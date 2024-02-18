import os
from typing_extensions import Text

import ffmpeg
import numpy as np
import speech_recognition as sr

from speech_recognition import Recognizer
from speech_recognition import AudioData





class Speech2Text():
    def __init__(self) -> None:
        self.temp_wav_file = os.path.join("temp","speech.wav")
        self.recognizer = sr.Recognizer()

        self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = str(os.path.join("data","cool-eye-269214-53f90e6f9d71.json"))
       
        self.language="zh-CN"

        # self.model = self._load_whispercpp_model()

    
    def speech_to_text( self, sample_rate=16000):
        audio_data =self._record(sample_rate=sample_rate)
        text =  self._transcribe(audio_data)
        return text

        

    def _record(self, sample_rate=16000)-> AudioData:
        """
        collect audio from mircophone by speech_recognition
        requires PyAudio because it uses the Microphone class

        https://pypi.org/project/SpeechRecognition/
        https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition
        https://realpython.com/python-speech-recognition/
        """
        
        with sr.Microphone(sample_rate=sample_rate) as source:
            # 校准环境噪音水平
            self.recognizer.adjust_for_ambient_noise(source,duration=1)
            print(f"You can stat to talk now")
            audio = self.recognizer.listen(source,timeout=15, phrase_time_limit=5)

        # if not os.path.exists(os.path.dirname(self.temp_wav_file)):
        #     os.makedirs(os.path.dirname(self.temp_wav_file))
        # with open(self.temp_wav_file,"wb") as f:
        #     f.write(audio.get_wav_data())
        # if if_cmu:
        #     return audio
        # else:
        #     return  _get_file_content(self.temp_wav_file)

        return audio
    
    def _transcribe(self, audio_data:AudioData):
        text = self._transcribe_by_google_cloud_speech_api(audio_data=audio_data)
        return text


    def _transcribe_by_google_cloud_speech_api(self, audio_data:AudioData):
        # recognize speech using Google Cloud Speech
        # GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
        try:
            
            text = self.recognizer.recognize_google_cloud(audio_data, 
                                                          credentials_json= self.GOOGLE_CLOUD_SPEECH_CREDENTIALS,
                                                          language=self.language)
            print(f"Google Cloud Speech thinks you said:\n{text} ")

        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
        
        return text


     


    def _load_whispercpp_model(self):
        """
        useing whispercpp:   
        https://github.com/ggerganov/whisper.cpp
        
        Cython bind for whispercpp
        https://github.com/stlukey/whispercpp.py
        models in  ~/.ggml-models/

        pybind11 for whispercpp
        model = Whisper.from_pretrained(model_name="tiny.en",basedir="models")
        https://github.com/aarnphm/whispercpp

        """
        from whispercpp import Whisper
        # using whipercpp.py
        model = Whisper("tiny")

        # using whipercpp
        # model = Whisper.from_pretrained(model_name="base",basedir="models")
        return model
    
    def _transcribe_by_whisperapp(self,model,audio_path):
        # try:
        #     y, _ = (
        #         ffmpeg.input(audio_path, threads=0).output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=sample_rate)
        #         .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
        #     )
        # except ffmpeg.Error as e:
        #     raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e
        # arr = np.frombuffer(y, np.int16).flatten().astype(np.float32) / 32768.0

        result = model.transcribe(audio_path)
        text = model.extract_text(result)
        return text






def _get_file_content(file_name):
    with open(file_name,"rb") as f:
        audio_data =  f.read()
    return audio_data
    

if __name__ == '__main__':
    model_path = "models/whispercpp/ggml-tiny.en.bin"
    audio_path = os.path.join("tutorials","whisper_cpp","samples","jfk.wav") # pathlib.Path(audio_path)
  

    speech2text = Speech2Text()
    speech2text.speech_to_text()
    




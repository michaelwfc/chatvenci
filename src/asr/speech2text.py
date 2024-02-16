import os
import ffmpeg
import numpy as np


import speech_recognition as sr
from typing_extensions import Text






class Speech2Text():
    def __init__(self) -> None:
        self.temp_wav_file = os.path.join("temp","speech.wav")
        self.recognizer = sr.Recognizer()

        self.model = self._load_whispercpp_model()

    def _record(self,if_cmu:bool =False, rate=16000)->sr.AudioData:
        """
        collect audio from mircophone by speech_recognition
        requires PyAudio because it uses the Microphone class

        https://pypi.org/project/SpeechRecognition/
        https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition
        https://realpython.com/python-speech-recognition/
        """
        
        with sr.Microphone(sample_rate=rate) as source:
            # 校准环境噪音水平
            self.recognizer.adjust_for_ambient_noise(source,duration=1)
            print(f"You can stat to talk now")
            audio = self.recognizer.listen(source,timeout=15, phrase_time_limit=5)


        if not os.path.exists(os.path.dirname(self.temp_wav_file)):
            os.makedirs(os.path.dirname(self.temp_wav_file))
        with open(self.temp_wav_file,"wb") as f:
            f.write(audio.get_wav_data())

        return audio
        # if if_cmu:
        #     return audio
        # else:
        #     return  _get_file_content(self.temp_wav_file)


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

        # from pywhispercpp.model import Model
        # model_path = os.path.join("models","whispercpp","ggml-base.bin")
        # model = Model(model_path, n_threads=6)
        # audio_path = os.path.join("tutorials","whispercpp.py", "whisper.cpp","samples","jfk.wav")
        # segments = model.transcribe(audio_path, speed_up=True)
        # for segment in segments:
        #     print(segment.text)
        return model



    def speech_to_text( self, audio_path:Text ,if_microphone:bool= False,sample_rate=16000):
        """
        model = "models/whispercpp/ggml-tiny.en.bin"
        audio_path = "tutorials\whisper_cpp\samples\jfk.wav"
        text = speech_to_text(audio_path=audio_path,model=model)
        """
        if if_microphone:
            text = None
        else:
            # try:
            #     y, _ = (
            #         ffmpeg.input(audio_path, threads=0).output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=sample_rate)
            #         .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
            #     )
            # except ffmpeg.Error as e:
            #     raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e
            # arr = np.frombuffer(y, np.int16).flatten().astype(np.float32) / 32768.0

            result = self.model.transcribe(audio_path)
            # text = model.extract_text(result)
            return text


def _get_file_content(file_name):
    with open(file_name,"rb") as f:
        audio_data =  f.read()
    return audio_data
    

if __name__ == '__main__':
    model_path = "models/whispercpp/ggml-tiny.en.bin"
    audio_path = os.path.join("tutorials","whisper_cpp","samples","jfk.wav") # pathlib.Path(audio_path)
  
    # text = speech_to_text(audio_path=audio_path,model=model)
    # print(f"text={text}")

    speech2text = Speech2Text()
    speech2text._record()
    




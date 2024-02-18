import os
from os import path
import speech_recognition as sr


os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = ""


def transcribe_from_audio():
    # obtain path to "english.wav" in the same folder as this script
    
    AUDIO_FILE = path.join(os.getcwd(), "temp","speech.wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source ) # read the entire audio file


    # recognize speech using Google Cloud Speech
    # GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = str(os.path.join("data","cool-eye-269214-53f90e6f9d71.json"))

    try:
        print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS,language="zh-CN"))
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
if __name__=="__main__":
    transcribe_from_audio()
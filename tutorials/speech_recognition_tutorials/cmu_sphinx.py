import os
from os import path
import speech_recognition as sr


def listen_from_microphone():
    # obtain audio from the microphone
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source,duration=1)

            print("Say something!")
            audio = recognizer.listen(source,timeout=15, phrase_time_limit=5)

        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + recognizer.recognize_sphinx(audio,language= "zh-CN"))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


def transcribe_from_audio():
    # obtain path to "english.wav" in the same folder as this script
    )
    AUDIO_FILE = path.join(os.getcwd(), "temp","speech.wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source  # read the entire audio file

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio,language= "zh-CN"))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        


if __name__=="__main__":
    sr_path = sr.__file__
    transcribe_from_audio()




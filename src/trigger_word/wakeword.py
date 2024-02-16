import os
import struct

import pvporcupine
import pyaudio

PICOVOICE_API_KEY = "+C/iqo1wpIdfd2QbtvFN1q0Cyywc6E/vznCOfVHqO5Ab0SWkaYtmkA=="

windows_path =  os.path.join("models","wakeword_models","Hey-Vinci_en_windows_v3_0_0","Hey-Vinci_en_windows_v3_0_0.ppn")
# s.path.join("models","wakeword_models","Vinci_en_linux_v3_0_0","Vinci_en_linux_v3_0_0.ppn")
KEYWORD_PATHS= [windows_path]


class PicoWakeWord():
    def __init__(self):
        """
        
        PyAudio package is needed for capturing microphone input.
        """
        self.picovoice_api_key = PICOVOICE_API_KEY
        self.keyword_paths = KEYWORD_PATHS
        self.porcupine = pvporcupine.create(access_key=self.picovoice_api_key, keyword_paths=self.keyword_paths)
        self.myaudio =  pyaudio.PyAudio()
        self.stream =  self.myaudio.open(
            input_device_index =0,
            rate = self.porcupine.sample_rate,
            channels=1,
            format= pyaudio.paInt16,
            input=True,
            frames_per_buffer = self.porcupine.frame_length
        )



    def detect_wake_word(self):
        print(f"detecting PICOVOICE wakeword model")
        while True:
            audio_obj = self.stream.read(self.porcupine.frame_length, exception_on_overflow=False)
            audio_obj_unpacked =  struct.unpack_from("h" * self.porcupine.frame_length, audio_obj)

            keyword_index = self.porcupine.process(audio_obj_unpacked)
            if keyword_index >=0:
                print(f"我听到了 keyword_index={keyword_index}")
                # return keyword_index


if __name__ == '__main__':
    pico_wake_word =PicoWakeWord()
    pico_wake_word.detect_wake_word()
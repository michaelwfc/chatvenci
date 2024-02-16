# Structure
- Trigger Word detection
- ASR
- NLP
- TTS

# Trigger Word detection module
1. train and download a wake word model on Picovoice官网: https://picovoice.ai/
2. pyaudio模块使用监听麦克风
https://people.csail.mit.edu/hubert/pyaudio/#downloads

windows 安装pyaudio: 
https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14

ubuntu:
```shell
$sudo apt-get install portaudio19-dev
```


# ASR module
1. C dev  on windows
install msys2/MinGW :  https://www.msys2.org/

2.  ffmpeg
- install ffmpeg on windows
https://ffmpeg.org/download.html#build-windows
winodws:  
downlaod ffmppeg + set env on windows

Ubuntu:
sudo apt install ffmpeg

- pip install ffmpeg-python
https://github.com/kkroening/ffmpeg-python


3. use whisper

- download whisper model and build whispercpp
https://github.com/openai/whisper
https://github.com/ggerganov/whisper.cpp
https://github.com/stlukey/whispercpp.py
https://github.com/aarnphm/whispercpp

on windows:
```shell
# open msys2 terminal
make
```

main.exe -m  models/ggml-base -f samples/jfk.wav
```




- python wrapper for whispercpp
    - pybind11 for whispercpp
    w = Whisper.from_pretrained(model_name="tiny.en",basedir="models")
    https://github.com/aarnphm/whispercpp

    - Cython bind for whispercpp
    intall msvc on windows
    https://code.visualstudio.com/docs/cpp/config-msvc

    https://github.com/stlukey/whispercpp.py
    models in  ~/.ggml-models/
    pip install git+https://github.com/stlukey/whispercpp.py

    on windows install whispercpp==1.0:
    git clone https://github.com/stlukey/whispercpp.py.git
    git clone https://github.com/ggerganov/whisper.cpp
    cd whisper.cpp
    git reset --hard  0a2d121
    cd ../whispercpp.py
    python setup.py install





# Automatic Speech Recognition(ASR)/ Speech TO Text (STT)
## open-source projects 
Here are some good open-source projects for speech to text with Python:
https://github.com/topics/speech-to-text

- whisper支持多语言，且效果非常好，但是缺点是速度慢，有 一些优化项目如fast whisper
- DeepSpeech: A deep learning-based speech recognition engine developed by Mozilla. It achieves state-of-the-art accuracy and can be trained on custom datasets.

- SpeechRecognition: A Python library that provides support for speech recognition using various APIs, including Google Speech Recognition, Microsoft Bing Speech, and CMU Sphinx.
[https://pypi.org/project/SpeechRecognition/]
[https://realpython.com/python-speech-recognition/]
- Julius: A large vocabulary continuous speech recognition engine that supports various languages. It is known for its high recognition accuracy and flexibility.
- Kaldi: A toolkit for speech recognition, speaker recognition, and natural language processing. It is widely used in research and development of speech technologies.
- CMU Sphinx: A speech recognition toolkit developed by Carnegie Mellon University. It supports various acoustic models and language models, and it can be used for both online and offline speech recognition.
- Wav2Letter++ 是一款由 Facebook 的 AI 研究团队

## related projects
- https://www.bilibili.com/video/BV1Ns4y1m7TH/?spm_id_from=333.880.my_history.page.click&vd_source=b3d4057adb36b9b243dc8d7a6fc41295
- https://github.com/MedalCollector/Orator


# env
```shell
python -m venv env
source env/Script/activate

pip install pvporcupine
python -m pip install pyaudio

# ASR
#pip install whispercpp
pip install numpy
pip install SpeechRecognition


```
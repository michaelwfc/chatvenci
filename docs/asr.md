
# ASR module
Automatic Speech Recognition(ASR)/ Speech TO Text (STT)
## open-source projects 
Here are some good open-source projects for speech to text with Python:
https://github.com/topics/speech-to-text


- SpeechRecognition: A Python library that provides support for speech recognition using various APIs, including Google Speech Recognition, Microsoft Bing Speech, and CMU Sphinx.
[https://pypi.org/project/SpeechRecognition/]
[https://realpython.com/python-speech-recognition/]
[speech_recognition](https://github.com/Uberi/speech_recognition)


- whisper支持多语言，且效果非常好，但是缺点是速度慢，有 一些优化项目如fast whisper  

- DeepSpeech: A deep learning-based speech recognition engine developed by Mozilla. It achieves state-of-the-art accuracy and can be trained on custom datasets.


- Julius: A large vocabulary continuous speech recognition engine that supports various languages. It is known for its high recognition accuracy and flexibility.

- Kaldi: A toolkit for speech recognition, speaker recognition, and natural language processing. It is widely used in research and development of speech technologies.
[Kaldi-github](https://github.com/kaldi-asr/kaldi)

- CMU Sphinx: A speech recognition toolkit developed by Carnegie Mellon University. It supports various acoustic models and language models, and it can be used for both online and offline speech recognition.  
效果比较差
- Wav2Letter++ 是一款由 Facebook 的 AI 研究团队



## Google Cloud Speech-to-Text
[Google-speech2text project](https://console.cloud.google.com/welcome?hl=zh-cn&project=cool-eye-269214)
[Speech-to-Text 价格](https://cloud.google.com/speech-to-text/pricing?hl=zh-cn)
### apply for speech-to-text api
[Google Cloud Speech-To-Text API With Python For Beginners](https://www.youtube.com/watch?v=izdDHVLc_Z0)
- build a project
- 控制台 > API&Severvice >  Cloud Speech-to-Text API > enable API 
-  控制台 > service account > build > key >add key > json

## whispercpp
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
main.exe -m  models/ggml-base -f samples/jfk.wav
main.exe -m  models/ggml-base -f samples/speech.wav -l zh
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
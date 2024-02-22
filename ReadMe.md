# Structure
- Trigger Word detection
- ASR
- NLP
- TTS

## related projects
[手把手教你做ChatGPT智能音箱](https://www.bilibili.com/video/BV1Ns4y1m7TH/?spm_id_from=333.880.my_history.page.click&vd_source=b3d4057adb36b9b243dc8d7a6fc41295)
- https://github.com/MedalCollector/Orator


# Features
- Voice chatbot
- Play online music
- Search and Play local music
- Retrival based QA
- Teach English 
- Tell Story for childrend
- Query Weather
- News
- IOT to other device



# env
```shell
python -m venv env
source env/Script/activate

# trigger word
pip install pvporcupine
python -m pip install pyaudio

# ASR
pip install numpy
pip install SpeechRecognition

## whispercpp with cython: to slow
# pip install cython

## using CMU Sphinx: too bad accuray
# pip install pocketsphinx

## using google-cloud-speech to text
pip install google-cloud-speech

# TTS
## use edge_tts
pip install edge_tts

## use azure-cognitiveservices-speech
# pip install azure-cognitiveservices-speech

# chat
## chat with openai api
pip install openai

```
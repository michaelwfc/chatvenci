from edge_tts import Communicate, VoicesManager
import pygame # 导入pygame，playsound报错或运行不稳定时直接使用
import asyncio

XIAOYI_NEURAL = "zh-CN-XiaoyiNeural"
XIAOXIAO_NEURAL = "zh-CN-XiaoxiaoNeural"
XIAOBEI_NEURAL = "zh-CN-liaoning-XiaobeiNeural"
XIAOCHEN_NEURAL ="zh-TW-HsiaoChenNeural"


class EdgeTTS:
    def __init__(self, voice: str =XIAOYI_NEURAL, rate: str = "+0%", volume: str = "+0%"):
        """
        rate参数可以通过加号或者减号同步加快或者减慢合成语音的语速。
        volume参数可以调整语音的音量
        和微软Azure官方的语音合成库相比，开源的语音合成库并不支持基于标记语言 (SSML)的语音调优，比如语调、情绪的调整

        """
        self.voice = voice
        self.rate = rate
        self.volume = volume

    async def text_to_speech_and_play(self, text):
        # voices = await VoicesManager.create()
        # voice = voices.find(Gender="Female", Language="zh")
        # communicate = edge_tts.Communicate(text, random.choice(voice)["Name"])
        communicate = Communicate(text, self.voice)
        await communicate.save('./temp/audio.mp3')
        # playsound('./audio.wav') # playsound无法运行时删去此行改用pygame，若正常运行择一即可
        self.play_audio_with_pygame('./temp/audio.mp3')  # 注意pygame只能识别mp3格式


    def play_audio_with_pygame(self, audio_file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()

    
    async def _find_voice(self):
        voices = await VoicesManager.create()
        voice = voices.find(Gender="Female", Language="zh") 
        return voice
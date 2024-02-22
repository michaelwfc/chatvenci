


def main():
    """
    1. trigger: wake word model
    2. asr: 
    3. chat:
    4. tts:
    """
    import asyncio
    from utils.environments import set_gpt_env
    set_gpt_env()

    from trigger_word.wakeword import PicoWakeWord
    from asr.speech2text import Speech2Text
    from chats.chat_with_gemini import chat_gemini_with_llm,ChatGemini
    from tts.text2speech import EdgeTTS

    pico_wake_word =PicoWakeWord()
    speech2text = Speech2Text()
    chat_gemini =ChatGemini()
    edgetts = EdgeTTS()

    print(f"start to listening from micorphone\n{'*'*100}")
    # initial sound
    asyncio.run(edgetts.text_to_speech_and_play("Hi,大家好啊！我叫 Venci"))
    while True:
        # 1. trigger
        keyword_index = pico_wake_word.detect_wake_word()
        if keyword_index>= 0:
            print(f"I deceted the trigger word, let's start to chat\n{'*'*100}")
            # say hello when triggered
            # asyncio.run(edgetts.text_to_speech_and_play("你好"))

            # reocord from microphone and do asr
            text = speech2text.record_and_transcribe()
            # chat 
            output_text = chat_gemini.chat(text)
            # tts
            asyncio.run(edgetts.text_to_speech_and_play(output_text))

if __name__ =="__main__":
    main()
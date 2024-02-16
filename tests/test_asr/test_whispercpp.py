import os


def test_whipercpppy():
    print(f"working_dir={os.getcwd()}")
    from whispercpp import Whisper

    w = Whisper('small')
    # audio_path = os.path.join("whispercpp.py", "whisper.cpp","samples","jfk.wav")
    audio_path = os.path.join("temp","speech.wav")
    
    result = w.transcribe(audio_path)
    text = w.extract_text(result)
    print(f"text={text}")

if __name__ =="__main__":
    test_whipercpppy()
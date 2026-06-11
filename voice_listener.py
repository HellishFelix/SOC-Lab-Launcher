import subprocess
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

from logger import write_log
from config import (
    WAKE_WORDS,
    MICROPHONE_ID
)

MODEL_PATH = "models/vosk-model-small-ru-0.22"

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

print("Listening...")
launcher_started=False

def callback(indata,frames,time,status):
    global launcher_started

    if recognizer.AcceptWaveform(bytes(indata)):
        result = json.loads(recognizer.Result())

        text = result.get("text", "")

        if text:
            
            if(
                all(word in text for word in WAKE_WORDS)
                and not launcher_started
            ):
                launcher_started = True

                print("\n[VOICE] Wake phrase detected!")
                write_log("VOICE: Wake phrase detected!")
                print("[VOICE] Starting SOC Lab...\n")
                write_log("VOICE: Starting SOC Lab")

                subprocess.Popen(
                    ["py", "main.py"]
                )

with sd.RawInputStream(
    device=MICROPHONE_ID,
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback
):
    input("Press Enter to stop...\n")
import subprocess
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import time

from logger import write_log
from config import (
    WAKE_WORDS,
    MICROPHONE_ID
)

write_log("VOICE: Listener started")

MODEL_PATH = "models/vosk-model-small-ru-0.22"

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

print("Listening...")

last_launch_time = 0

def callback(indata, frames, callback_time, status):
    global last_launch_time

    if recognizer.AcceptWaveform(bytes(indata)):
        result = json.loads(recognizer.Result())

        text = result.get("text", "")

        if text:
            
            if(
                all(word in text for word in WAKE_WORDS)
                and time.time() - last_launch_time > 10
            ):
                last_launch_time = time.time()

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
    while True:
        time.sleep(1)
# speech_engine.py
import pyttsx3
import time
from config import TTS_RATE, TTS_VOLUME, REPEAT_DELAY

engine = pyttsx3.init()
engine.setProperty('rate', TTS_RATE)
engine.setProperty('volume', TTS_VOLUME)

last_spoken = {}

def speak(label):
    current_time = time.time()
    if label not in last_spoken or (current_time - last_spoken[label]) > REPEAT_DELAY:
        engine.say(label)
        engine.runAndWait()
        last_spoken[label] = current_time

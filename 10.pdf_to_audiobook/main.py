"""
PDF to audiobook
"""
import pyttsx3

engine = pyttsx3.init()

with open("text_files/test.txt") as file:
    lines = file.read()
    engine.say(lines)

engine.runAndWait()

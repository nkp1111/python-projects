"""
PDF to audiobook
"""
import pyttsx3

engine = pyttsx3.init()

# speech rate or speed of speech delivery defaults 200
print(engine.getProperty("rate"))
speech_rate_or_speed = 150
engine.setProperty("rate", speech_rate_or_speed)

# volume (0, 1) defaults 1
print(engine.getProperty("volume"))
speech_volume = 1.2
engine.setProperty("volume", speech_volume)

# voices male or female
voices = engine.getProperty("voices")
male_voice = voices[0].id
female_voice = voices[1].id
engine.setProperty("voice", female_voice)

with open("text_files/test.txt") as file:
    lines = file.read()
    # engine.say(lines)
    filename = input("Type a filename for this audio file: ")
    engine.save_to_file(lines, f"audio_files/{filename}.mp3")

engine.runAndWait()

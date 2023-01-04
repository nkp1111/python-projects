"""
Take pdf or txt file and converts it into audiobook
Required 'pyttsx3' and 'PyPDF2' modules
"""
import pyttsx3
import PyPDF2


def create_audio_book(filename, volume, speed, voice, start, end):
    engine = pyttsx3.init()

    engine.setProperty("rate", speed)
    engine.setProperty("volume", volume)

    voices = engine.getProperty("voices")
    male_voice = voices[0].id
    female_voice = voices[1].id
    if voice == "Male":
        engine.setProperty("voice", male_voice)
    else:
        engine.setProperty("voice", female_voice)

    text_content = ""
    if filename.endswith(".pdf"):
        with open(filename, mode="rb") as file:
            book = PyPDF2.PdfReader(file)
            total_page = len(book.pages)
            first_page = max(0, start)
            last_page = total_page if end < 0 else min(total_page, end)
            for page_num in range(first_page, last_page):
                print(f"reading file {page_num}")
                page = book.pages[page_num]
                text_content += page.extract_text()
    else:
        with open(filename) as file:
            text_content = file.read()

    print("converting file")
    converted_file = f"audio_files/{filename.split('/')[-1][:-3]}mp3"
    engine.save_to_file(text_content, converted_file)
    engine.runAndWait()
    return converted_file


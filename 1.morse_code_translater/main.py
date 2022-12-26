# Morse Code Translater
# Translate a string into morse code
from art import logo


def morse_code_converter(string):
    string_code = {
        "A": "._",
        "N": "_.",
        "B": "_...",
        "O": "___",
        "C": "_._.",
        "P": ".__.",
        "D": "_..",
        "Q": "__._",
        "E": ".",
        "R": "._.",
        "F": ".._.",
        "S": "...",
        "G": "__.",
        "T": "_",
        "H": "....",
        "U": ".._",
        "I": "..",
        "V": "..._",
        "J": ".___",
        "W": ".__",
        "K": "_._",
        "X": "_.._",
        "L": "._..",
        "Y": "_.__",
        "M": "__",
        "Z": "__..",
        "1": ".____",
        "6": "_....",
        "2": "..___",
        "7": "__...",
        "3": "...__",
        "8": "___..",
        "4": "...._",
        "9": "____.",
        "5": ".....",
        "0": "_____",
        "=": "_..._",
        "+": "._._.",
        ",": "__..__",
        ".": "._._._",
        "?": "..__..",
        ";": "_._._.",
        "-": "_...._",
        "'": ".____.",
        "@": ".__._.",
        "(": "_.__.",
        ")": "_.__._"
    }

    morse_code = ""
    for s in string:
        morse_code += string_code.get(s.upper(), s) + " "
    return morse_code.rstrip()


print("Welcome to Morse Code Translater...")
print(logo)

word = input("Input word you want to convert to morse code: \n")
print(f"The morse code of the '{word}' is:\n \"{morse_code_converter(word)}\"")

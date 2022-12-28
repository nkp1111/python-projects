"""
This program will show a paragraph to type.
Allow one minute for typing
Checks the correct number of words typed.
And print out the result.
"""
from tkinter import Tk, Text, Label, Entry, DISABLED, END, NORMAL
from tkinter import messagebox
from paragraph import para

DARK_BLUE = "#2B3A55"
BRIGHT_YELLOW = "#FFB100"
LIGHT_CREAM = "#F2E5E5"
TYPING_TIME = 60 * 1000

current_text = 0
current_word = 0
correct_word = 0
words = para.split(" ")
timer = None


# --------------------------------------------------------------------
# start typing
def start_typing(key):
    """
    Start timer, calculate score and remove old highlights
    :param key:
    :return:
    """
    global current_word, correct_word, timer, current_text

    if timer is None:
        timer = window.after(TYPING_TIME, show_result)
    if key.char == " ":
        current_word_length = len(words[current_word])
        para_to_type.tag_remove("start", index1=f"1.{current_text}", index2=f"1.{current_text + current_word_length}")
        text = typing_field.get()
        if text.strip() == words[current_word]:
            correct_word += 1

        typing_field.delete(0, END)
        current_word += 1
        current_text += current_word_length + 1

        highlight_text()
        change_line()


def highlight_text():
    """
    Highlight current text to type
    :return:
    """
    global current_text, current_word
    current_word_length = len(words[current_word])
    para_to_type.tag_add("start", f"1.{current_text}", f"1.{current_text + current_word_length}")
    para_to_type.tag_config("start", background=BRIGHT_YELLOW, foreground=DARK_BLUE)


def show_result():
    """
    Show result at end
    :return:
    """
    score = (correct_word * TYPING_TIME) // (60 * 1000)
    window.after_cancel(timer)
    messagebox.showinfo(title="Score", message=f"Final Score: {score} per minute")
    window.destroy()
    print(f"You final score is {score} per minute")


def change_line():
    """
    Change line in paragraph to see text properly
    :return:
    """
    global words, current_word, current_text
    if current_word and current_word % 5 == 0:
        words = words[current_word:]
        para_to_type.config(state=NORMAL)
        para_to_type.delete("1.0", END)
        para_to_type.insert("1.0", " ".join(words))
        para_to_type.config(state=DISABLED)

        current_text = 0
        current_word = 0
        highlight_text()


# --------------------------------------------------------------------
# tkinter components
# window screen
window = Tk()
window.title("Typing Speed Test")
window.minsize(300, 300)
window.config(
    padx=50,
    pady=50,
    bg=LIGHT_CREAM,
)

# heading
heading = Label(text="Typing Speed Test", font=("Roboto", 40, "bold"))
heading.config(
    fg=DARK_BLUE,
    bg=LIGHT_CREAM,
    highlightthickness=0
)
heading.grid(row=0, column=0, columnspan=2, pady=40)

# paragraph to type
para_to_type = Text(window, width=40, height=3, font=("Arial", 20))
para_to_type.insert("1.0", para)
para_to_type.config(state=DISABLED, padx=20, pady=20)
para_to_type.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

# input field
typing_field = Entry()
typing_field.config(
    width=30,
    bg="#fff",
    font=("Arial", 15, "normal"),
)
typing_field.focus()
typing_field.grid(row=2, column=0, columnspan=2, pady=20, padx=20, ipady=10, ipadx=50)

window.bind("<KeyPress>", start_typing)

highlight_text()
window.mainloop()

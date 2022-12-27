"""
This program will show a paragraph to type.
Allow one minute for typing
Checks the correct number of words typed.
And print out the result.
"""
from tkinter import Tk, Text, Label, Entry, DISABLED, END
from tkinter import messagebox
from paragraph import para

DARK_BLUE = "#2B3A55"
LIGHT_RED = "#CE7777"
LIGHT_CREAM = "#F2E5E5"
current_text = 0
current_word = 0
correct_word = 0
words = para.split(" ")
timer = None


# --------------------------------------------------------------------
# start typing
def start_typing(key):
    global current_word, correct_word, timer

    if timer is None:
        timer = window.after(10000, show_result)
    if key.char == " ":
        text = typing_field.get()
        if text.strip() == words[current_word]:
            correct_word += 1

        typing_field.delete(0, END)
        current_word += 1
        highlight_text()


def highlight_text():
    global current_text, current_word
    current_word_length = len(words[current_word])
    para_to_type.tag_add("start", f"1.{current_text}", f"1.{current_word_length}")
    para_to_type.tag_config("start", background=LIGHT_CREAM, foreground=DARK_BLUE)
    current_text += current_word_length + 1


def show_result():
    print(correct_word)
    window.after_cancel(timer)
    messagebox.showinfo(title="Score", message=f"Final Score: {correct_word}")
    window.destroy()


# --------------------------------------------------------------------
# tkinter components
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

# paragraph
para_to_type = Text(window, width=40, height=3, font=("Arial", 20))
para_to_type.insert("1.0", para)
para_to_type.config(state=DISABLED, padx=20, pady=20)
para_to_type.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

# input field
typing_field = Entry()
typing_field.config(
    width=50,
    bg="#fff",
    font=("Arial", 15, "normal"),
)
typing_field.focus()
typing_field.grid(row=2, column=0, columnspan=2, pady=20, padx=20, ipady=10, ipadx=50)

window.bind("<KeyPress>", start_typing)

highlight_text()
window.mainloop()

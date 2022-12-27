"""
This is graphical user interface application.
Ask for image file and watermark text.
Give new image with watermark text.
"""
from tkinter import Tk, Label, Entry, Button, END
from PIL import Image, ImageDraw, ImageFont


# from tkinter.messagebox import showinfo


# **********************************************/
def begin_draw(width, height, image, text):
    """
    Draw watermark on image
    :return:
    """
    img_draw = ImageDraw.Draw(image)
    img_draw.text((50, 50), text, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 35))
    img_name = image.filename.split("/")[-1]
    image.save(f"watermarked_images/wm-{img_name}")


# **********************************************/
# add watermark function
def add_watermark():
    """
    Add watermark to image
    :return:
    """
    img_file = image_input.get()
    watermark = wm_input.get()
    img = Image.open(img_file)
    width, height = img.size
    begin_draw(width, height, img, watermark)


# **********************************************/
# Tkinter components
NIGHT_BLUE = "#1C315E"
TEAL = "#227C70"
LAWN_GREEN = "#88A47C"
CREAM = "#E6E2C3"
HEADING_FONT = ("Arial", 30, "bold")

window = Tk()
window.title("Watermark Logo")
window.config(
    background=NIGHT_BLUE,
    padx=50,
    pady=50
)
window.minsize(500, 500)

# main heading
heading = Label(text="Watermark Logo")
heading.config(bg=NIGHT_BLUE, fg=CREAM, highlightthickness=0, font=HEADING_FONT)
heading.grid(row=0, column=0, columnspan=2, pady=30)

# input field for image file
img_label = Label(text="Provide image file path: ")
img_label.config(bg=NIGHT_BLUE, fg=CREAM, highlightthickness=0, font=("Ariel", 15))
img_label.grid(row=3, column=0, pady=10)

image_input = Entry()
image_input.focus()
image_input.insert(0, "images/cat-wall.jpg")
image_input.config(width=50)
image_input.grid(row=3, column=1)

# watermark text input field
wm_text_label = Label(text="Add watermark text: ")
wm_text_label.config(bg=NIGHT_BLUE, fg=CREAM, highlightthickness=0, font=("Ariel", 15))
wm_text_label.grid(row=4, column=0)

wm_input = Entry()
wm_input.insert(0, "Watermark logo")
wm_input.config(width=50)
wm_input.grid(row=4, column=1)

# submit button
submit_btn = Button(text="Confirm")
submit_btn.config(command=add_watermark)
submit_btn.grid(row=5, column=1, pady=20)

window.mainloop()

"""
This is graphical user interface application.
Ask for image file and watermark text.
Give new image with watermark text.
"""
from tkinter import Tk, Label, Entry, Button, END
from PIL import Image, ImageDraw, ImageFont


# **********************************************/
# add watermark function
def add_watermark():
    """
    Add watermark to image and save it into watermarked_images folder.
    :return:
    """
    img_file = image_input.get()
    watermark = wm_input.get()
    img = Image.open(img_file)
    img_draw = ImageDraw.Draw(img)
    img_draw.text((50, 50),
                  text=watermark,
                  fill=(0, 0, 0),
                  font=ImageFont.truetype("arial.ttf", 40),
                  stroke_fill="white",
                  stroke_width=3)
    img_name = img.filename.split("/")[-1]
    img.save(f"watermarked_images/wm-{img_name}")


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
heading.config(bg=NIGHT_BLUE, fg=CREAM,
               highlightthickness=0, font=HEADING_FONT)
heading.grid(row=0, column=0, columnspan=2, pady=30)

# input field for image file
img_label = Label(text="Image file path: ")
img_label.config(bg=NIGHT_BLUE, fg=CREAM,
                 highlightthickness=0, font=("Ariel", 15))
img_label.grid(row=3, column=0, pady=10)

image_input = Entry()
image_input.focus()
image_input.insert(0,  "images/cat-wall.jpg")
image_input.config(width=50)
image_input.grid(row=3, column=1)

# watermark text input field
wm_text_label = Label(text="Watermark text: ")
wm_text_label.config(bg=NIGHT_BLUE, fg=CREAM,
                     highlightthickness=0, font=("Ariel", 15))
wm_text_label.grid(row=4, column=0)

wm_input = Entry()
wm_input.insert(0, "Watermark logo")
wm_input.config(width=50)
wm_input.grid(row=4, column=1)

# submit button
submit_btn = Button(text="Confirm")
submit_btn.config(
    width=30,
    height=2,
    command=add_watermark,
    bg=CREAM,
)
submit_btn.grid(row=5, column=0, columnspan=2, pady=30)

window.mainloop()

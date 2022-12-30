"""
Color picker
Takes an image as input and print 10 top most common colors on it.
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired
from werkzeug.utils import secure_filename

from color_separator import get_top_colors

app = Flask(__name__)
app.config["SECRET_KEY"] = "sdlfkhs98wthh894t4ui"
Bootstrap(app)
STATIC_IMAGE_PATH = "images/cat-wall.jpg"


class ImageForm(FlaskForm):
    image = FileField(label="File to upload: ",
                      validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images Only!")])
    number = IntegerField(label="Number of colors: ", validators=[DataRequired()], default=10)
    submit = SubmitField(label="Run")


@app.route("/", methods=["GET", "POST"])
def home():
    form = ImageForm()
    if form.validate_on_submit():
        filename = secure_filename(form.image.data.filename)
        image_path_relative_static = "images/" + filename
        image_path_full = "static/" + image_path_relative_static
        form.image.data.save(image_path_full)
        color_numbers = form.number.data
        top_colors = get_top_colors(image_path_full, color_numbers)
        print(top_colors)
        return render_template("index.html", form=form, colors=top_colors, image=image_path_relative_static)
    else:
        top_colors = get_top_colors("static/" + STATIC_IMAGE_PATH, 10)

    return render_template("index.html", form=form, colors=top_colors, image=STATIC_IMAGE_PATH)


if __name__ == "__main__":
    app.run(debug=True)



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

from color_separator import get_top_colors

app = Flask(__name__)
app.config["SECRET_KEY"] = "sdlfkhs98wthh894t4ui"
Bootstrap(app)


class ImageForm(FlaskForm):
    image = FileField(label="File to upload: ",
                      validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images Only!")])
    number = IntegerField(label="Number of colors: ", validators=[DataRequired()], default=10)
    submit = SubmitField(label="Run")


@app.route("/", methods=["GET", "POST"])
def home():
    form = ImageForm()
    if form.validate_on_submit():
        top_colors = get_top_colors()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)



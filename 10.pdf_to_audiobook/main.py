"""
PDF to audiobook
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# form imports
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField, FileField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "KSLlsgj9459835yiu34j4k53kj"
Bootstrap(app)


# form
class BookForm(FlaskForm):
    pdf = FileField(label="Add a pdf/txt file: ",
                    validators=[FileRequired(), FileAllowed(["pdf", "txt"], "only pdf and text file")])
    speech_speed = SelectField(label="Speech speed: ",
                               choices=[100, 150, 200, 250, 300],
                               default=200)
    voices = SelectField(label="Speech voices(M/F): ",
                         choices=["Male", "Female"],
                         default="Male")
    speech_volume = SelectField(label="Speech volume: ",
                                choices=[0.5, 0.75, 1, 1.25, 1.5],
                                default=1)
    page_num = IntegerField(label="Number of pages(type -1 for whole book): ")
    submit = SubmitField(label="Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    form = BookForm()
    if form.validate_on_submit():
        print("pass")
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

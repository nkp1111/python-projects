"""
PDF to audiobook
"""
from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
# form imports
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField, FileField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired
# werkzeug utility
from werkzeug.utils import secure_filename
# text to speech
from text_to_speech import create_audio_book

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
    voices = SelectField(label="Speech voice (M/F): ",
                         choices=["Male", "Female"],
                         default="Male")
    speech_volume = SelectField(label="Speech volume: ",
                                choices=[0.5, 0.75, 1, 1.25, 1.5],
                                default=1)
    start_page = IntegerField(label="Page number to start with (e.g. 0): ",
                              default=0)
    end_page = IntegerField(label="Page number to end with (-1 for last): ", default=-1)
    submit = SubmitField(label="Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    form = BookForm()
    if form.validate_on_submit():
        filename = secure_filename(form.pdf.data.filename)
        filepath = f"text_files/{filename}"
        form.pdf.data.save(filepath)

        volume = int(form.speech_volume.data)
        speed = int(form.speech_speed.data)
        voice = form.voices.data
        start = form.start_page.data
        end = form.end_page.data
        converted_file = create_audio_book(filepath, volume, speed, voice, start, end)
        if converted_file:
            return send_from_directory("audio_files", filename[:-3] + "mp3", as_attachment=True)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

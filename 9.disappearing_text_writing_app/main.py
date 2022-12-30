"""
Disappearing text writing app
An app that allows the user to type but if user stops for 5-10 seconds all the words disappears.
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "LGHShjshjs8s74543h45hjdskhksgu"
Bootstrap(app)


class MyForm(FlaskForm):
    text = CKEditorField(render_kw={"placeholder": "Start Typing here"})


@app.route("/")
def home():
    form = MyForm()
    print(form.text.data)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

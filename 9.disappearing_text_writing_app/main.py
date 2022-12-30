"""
Disappearing text writing app
An app that allows the user to type but if user stops for 5-10 seconds all the words disappears.
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

"""
PDF to audiobook
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config["SECRET_KEY"] = "KSLlsgj9459835yiu34j4k53kj"
Bootstrap(app)


# form

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


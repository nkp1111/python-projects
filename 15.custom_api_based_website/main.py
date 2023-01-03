"""
Custom API based website
Show stock market data based on symbol
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from dotenv.main import DotEnv


dot = DotEnv(".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = dot.get("SECRET_KEY")
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

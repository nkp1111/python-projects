from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from project_data import my_projects, flask_projects

app = Flask(__name__)
app.config["SECRET_KEY"] = "28436h45hsgishgjshg89sgy"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html", projects=my_projects, flask_projects=flask_projects)


if __name__ == "__main__":
    app.run(debug=True)

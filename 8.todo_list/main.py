"""
Todo List website
Allows to add task, check completed task, delete task, update task
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from form import AddTaskForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "er54hgr9eiu459473y663o6h36ig6i3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_list.db"
Bootstrap(app)
db = SQLAlchemy(app)


# ---------------------------------------
#  database
class ToDoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    deadline = db.Column(db.DateTime)


with app.app_context():
    db.create_all()


# ---------------------------------------
# flask app routes
@app.route("/", methods=["GET", "POST"])
def home():
    form = AddTaskForm()
    if form.validate_on_submit():
        with app.app_context():
            new_task = ToDoTask(
                task=form.task.data,
                completed=False,
            )
            db.session.add(new_task)
            db.session.commit()
        form.task.data = ""

    with app.app_context():
        task_list = db.session.query(ToDoTask).all()

    return render_template("index.html", form=form, tasks=task_list)


if __name__ == "__main__":
    app.run(debug=True)

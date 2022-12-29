"""
Todo List website
Allows to add task, check completed task, delete task, update task
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from form import AddTaskForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "er54hgr9eiu459473y663o6h36ig6i3"
Bootstrap(app)

task_list = []


@app.route("/", methods=["GET", "POST"])
def home():
    form = AddTaskForm()
    if form.validate_on_submit():
        task_list.append(form.task.data)
        form.task.data = ""
    return render_template("index.html", form=form, tasks=task_list)


if __name__ == "__main__":
    app.run(debug=True)

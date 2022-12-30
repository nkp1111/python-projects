"""
Todo List website
Allows to add task, check completed task, delete task, update task
"""
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship

from form import AddTaskForm, RegisterForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "er54hgr9eiu459473y663o6h36ig6i3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_list.db"
Bootstrap(app)
db = SQLAlchemy(app)

current_tasks = []

# ---------------------------------------
#  database
class ToDoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    deadline = db.Column(db.DateTime)
    user = relationship('User', back_populates='tasks')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    tasks = relationship("ToDoTask", back_populates='user')


with app.app_context():
    db.create_all()


# ---------------------------------------
# flask app routes
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Show all tasks and add new tasks
    :return:
    """
    form = AddTaskForm()
    if form.validate_on_submit():
        with app.app_context():
            new_task = ToDoTask(
                task=form.task.data.capitalize(),
                completed=False,
            )
            db.session.add(new_task)
            db.session.commit()
        form.task.data = ""

    with app.app_context():
        task_list = db.session.query(ToDoTask).all()

    return render_template("index.html", form=form, tasks=task_list)


@app.route("/change_status/<int:task_id>")
def change_task_status(task_id):
    """
    Change task status (completed )
    :param task_id:
    :return:
    """
    with app.app_context():
        task = ToDoTask.query.get(task_id)
        if task.completed:
            task.completed = False
        else:
            task.completed = True
        db.session.commit()

    return redirect(url_for("home"))


@app.route("/add_date/<int:task_id>", methods=["GET", "POST"])
def add_deadline(task_id):
    """
    Update deadline for task
    :param task_id:
    :return:
    """
    if request.method == "POST":
        date = request.form.get("date")
        if date:
            with app.app_context():
                task = ToDoTask.query.get(task_id)
                task.deadline = datetime.strptime(date, "%Y-%m-%dT%H:%M")
                db.session.commit()
        return redirect(url_for('home'))

    return render_template("add_deadline.html", task_id=task_id)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    """
    Delete a task
    :param task_id:
    :return:
    """
    with app.app_context():
        task_to_delete = ToDoTask.query.get(task_id)
        db.session.delete(task_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


# ----------
# user route
@app.route("/register", methods=["GET", "POST"])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        with app.app_context():
            tasks = ToDoTask.query.filter_by(user_id=None).all()
            new_user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
                tasks=tasks
            )
            db.session.add(new_user)
            db.session.commit()
            # print("login user")

        return redirect(url_for('home'))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash("You have to register first.")
            return redirect(url_for("register_user"))
        if user and user.password != form.password.data:
            flash("Incorrect password.")
            return redirect(url_for("login_user"))
        else:
            print(f"Welcome, {user.name}")
            return redirect(url_for("home"))

    return render_template("register.html", form=form, login="true")


@app.route("/logout")
def logout_user():
    print("logout user")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

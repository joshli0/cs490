import flask
from .landing import landing

# Teacher pages
def manage_questions():
    return flask.render_template("manage_questions.html")

def manage_exams():
    return flask.render_template("manage_exams.html")

def grade_exams():
    return flask.render_template("grade_exams.html")

# Student pages
def take_exam():
    return flask.render_template("take_exam.html")

def view_results():
    return flask.render_template("view_results.html")

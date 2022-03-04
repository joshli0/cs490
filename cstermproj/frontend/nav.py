import flask
from .landing import landing

# Teacher pages
def manage_questions():
    return flask.render_template("manage_questions.html")

def manage_exams():
    return flask.render_template("manage_exams.html")

def grade_exams():
    return flask.render_template("grade_exams.html")

def review_exam():
	return flask.render_template("review_exam.html")

# Student pages
def exam_list():
    return flask.render_template("exam_list.html")

def view_results():
    return flask.render_template("view_results.html")

def take_exam():
    return flask.render_template("take_exam.html")

def results():
    return flask.render_template("results.html")

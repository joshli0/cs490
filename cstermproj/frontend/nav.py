import flask
from .landing import landing
from ..backend.questions import *
from ..backend.tests import *

# Teacher pages
def manage_questions():
    return flask.render_template("manage_questions.html",
    categories=get_categories(),
    difficulties=get_difficulties(),
    questionBank=get_all_questions(),
    questionid=get_question_ids())

def manage_exams():
    return flask.render_template("manage_exams.html",
    examNames=get_test_names())

def build_exam():
    return flask.render_template("build_exam.html",
    categories=get_categories(),
    difficulties=get_difficulties(),
    questionBank=get_all_questions(),
    id=get_question_ids())

def grade_exams():
    return flask.render_template("grade_exams.html",
    testResponses=get_all_responses())

def review_exam():
	return flask.render_template("review_exam.html",
    responses=get_all_responses())

# Student pages
def exam_list():
    return flask.render_template("exam_list.html",
    examNames=get_test_names())

def view_results():
    return flask.render_template("view_results.html")

def take_exam():
    return flask.render_template("take_exam.html",
    examQuestions=get_questions_and_points(name_or_id))

def results():
    return flask.render_template("results.html")

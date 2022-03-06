import flask
from flask import request
from .landing import landing
from ..middleend.testSend import *
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
    name = request.args.get('title')
    examID = get_test_id(name)
    return flask.render_template("build_exam.html",
    name = name,
    examID = examID,
    categories=get_categories(),
    difficulties=get_difficulties(),
    id=get_question_ids(),
    examQuestions=getquestionsintest(examID),
    questionBank=getQuestionNotInTest(examID))

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
    name = request.args.get('title')
    examID = get_test_id(name)
    return flask.render_template("take_exam.html",
    name = name,
    examID = examID,
    id=get_question_ids(),
    examQuestions=getquestionsintest(examID))

def results():
    return flask.render_template("results.html")

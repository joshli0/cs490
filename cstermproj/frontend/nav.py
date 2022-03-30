import flask
from flask import request
from .landing import landing
from ..middleend.testSend import *
from ..backend.questions import *
from ..backend.tests import *

def get_filters():
    category_filter = None
    difficulty_filter = None
    keyword_filter = None
    
    if "category" in request.args:
        category_filter = request.args["category"]
    
    if "difficulty" in request.args:
        difficulty_filter = request.args["difficulty"]
    
    if "keywords" in request.args:
        keyword_filter = request.args["keywords"]
    
    if category_filter is not None and category_filter.lower() == "none":
        category_filter = None
    
    if difficulty_filter is not None and difficulty_filter.lower() == "none":
        difficulty_filter = None
    
    if keyword_filter is not None and len(keyword_filter) == 0:
        keyword_filter = None
    
    return { "title_or_desc_substring": keyword_filter, "category": category_filter, "difficulty": difficulty_filter }

# Teacher pages
def show_questions():
    return flask.render_template("show_questions.html",
    categories=get_categories(),
    difficulties=get_difficulties(),
    questionBank=get_all_questions(**get_filters()),
    questionid=get_question_ids())

def manage_questions():
    return flask.render_template("manage_questions.html",
    categories=get_categories(),
    difficulties=get_difficulties(),
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
    questionBank=getQuestionNotInTest(examID, **get_filters()))

def grade_exams():
    return flask.render_template("grade_exams.html",
    submittedExams=get_submitted_exam_names_and_student_names())

def review_exam():
    name = request.args.get('exam')
    student = request.args.get('student')
    examID = get_test_id(name)
    questions = getquestionsintest(examID)
    commentsPerQuestion,wholeTestComments=get_test_comments(examID, student)
    autograderPoints=get_test_auto_grades(examID, student)
    scorePerQuestion=[sum(val) for val in autograderPoints]
    return flask.render_template("review_exam.html",
    name = name,
    student = student,
    examID = examID,
    questions=questions,
    commentsPerQuestion=commentsPerQuestion,
    wholeTestComments=wholeTestComments,
    autograderPoints=autograderPoints,
    scorePerQuestion=scorePerQuestion,
    answers=getTestResponses(examID, student),
    code_outputs=get_test_case_outputs(examID, student),
    function_names=get_test_response_actual_function_names(examID, student),
    manualPoints=get_test_manual_grades(examID, student),
    scoreTotal=sum(scorePerQuestion),
    scoreMax=sum(q["points"] for q in questions),
    detectedConstraints=get_test_response_detected_constraints(examID, student))

# Student pages
def exam_list():
    return flask.render_template("exam_list.html",
    examNames=get_available_test_names())

def view_results():
    return flask.render_template("view_results.html",
    examList=get_reviewable_tests())

def take_exam():
    name = request.args.get('title')
    examID = get_test_id(name)
    return flask.render_template("take_exam.html",
    name = name,
    examID = examID,
    examQuestions=getquestionsintest(examID))

def results():
    name = request.args.get('title')
    student = flask.session['user']
    examID = get_test_id(name)
    questions = getquestionsintest(examID)
    commentsPerQuestion,wholeTestComments=get_test_comments(examID, student)
    points=get_test_manual_grades(examID, student)
    scorePerQuestion=[sum(val) for val in points]
    autograderPoints=get_test_auto_grades(examID, student)
    return flask.render_template("results.html",
    name = name,
    student = student,
    examID = examID,
    questions=questions,
    commentsPerQuestion=commentsPerQuestion,
    wholeTestComments=wholeTestComments,
    scorePerQuestion=scorePerQuestion,
    answers=getTestResponses(examID, student),
    code_outputs=get_test_case_outputs(examID, student),
    function_names=get_test_response_actual_function_names(examID, student),
    points=points,
    autograderPoints=autograderPoints,
    scoreTotal=sum(scorePerQuestion),
    scoreMax=sum(q["points"] for q in questions),
    detectedConstraints=get_test_response_detected_constraints(examID, student))

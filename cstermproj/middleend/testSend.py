import flask
from ..backend.tests import *
from ..backend.questions import *
from ..backend.login import *
from flask import Flask, request, redirect

def send(flaskapp):
    @flaskapp.route("/create_test", methods = ["POST", "GET"])
    def createTest():
        data = request.values
        redir = "manage_exams"
        if 'examname' in data:
            name = data['examname']
            create_test(name)
            redir = "build_exam&title=" + name

        return redirect('/app?page=' + redir)

    @flaskapp.route("/add_question", methods = ["POST", "GET"])
    def addQuestion():
        data = request.values
        redir = "manage_exams"
        if 'test_id' in data and 'question_id' in data and \
            'point_value' in data:
            test_id = int(data['test_id'])
            question_id = int(data['question_id'])
            point_value = int(data['point_value'])
            add_question(test_id, question_id, point_value)
            redir = "build_exam&title=" + get_test_name(test_id)

        return redirect('/app?page=' + redir)

    @flaskapp.route("/remove_question", methods = ["POST", "GET", "DELETE"])
    def removeQuestion():
        data = request.values
        if 'test_id' in data and 'question_id' in data and \
            'point_value' in data:
            test_id = data['test_id']
            question_id = data['question_id']
            remove_question(test_id, question_id)

        return redirect('/app?page=manage_exams')

    @flaskapp.route("/delete_test", methods = ["POST", "GET", "DELETE"])
    def deleteTest():
        data = request.values
        if 'name' in data:
            name = data['name']
            delete_test(name)

        return redirect('/app?page=manage_exams')

    @flaskapp.route("/set_test_comments", methods = ["POST", "GET"])
    def setTestComments():
        data = request.values
        if 'name_or_id'in data and 'student_name'in data and \
            'comments_on_questions' in data and 'comments_on_whole_test' in data:
            name_or_id = data['name_or_id']
            student_name = data['student_name']
            comments_on_questions = data['comments_on_questions']
            comments_on_whole_test = data['comments_on_whole_test']
            set_test_comments(name_or_id, student_name, comments_on_questions, comments_on_whole_test)

        return redirect('/app?page=grade_exams')

    @flaskapp.route("/set_test_manual_grades", methods = ["POST", "GET"])
    def setTestManualGrades():
        data = request.values
        if 'name_or_id'in data and 'student_name_or_id' in data and \
            'manual_grades' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name']
            manual_grades = data['manual_grades']
            set_test_manual_grades(name_or_id, student_name_or_id, manual_grades)

        return redirect('/app?page=grade_exams')

    @flaskapp.route("/set_test_auto_grades", methods = ["POST", "GET"])
    def setTestAutoGrades():
        data = request.values
        if 'name_or_id'in data and 'student_name_or_id' in data and \
            'auto_grades' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name']
            auto_grades = data['auto_grades']
            set_test_auto_grades(name_or_id, student_name_or_id, auto_grades)

        return redirect('/app?page=grade_exams')

    @flaskapp.route("/set_test_grades_released", methods = ["POST", "GET"])
    def setTestGradesReleased():
        data = request.values
        if 'name_or_id'in data and 'student_name_or_id' in data and \
            'released' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name']
            released = data['released']
            set_test_auto_grades(name_or_id, student_name_or_id, released)

        return redirect('/app?page=grade_exams')

    @flaskapp.route("/submit_test_response", methods = ["POST", "GET"])
    def submitTestResponse():
        data = request.values
        if 'name_or_id'in data:
            name_or_id = data['name_or_id']
            student_name_or_id = flask.session['user']

            responses = []
            for i in range (len(get_questions_and_points(name_or_id)[0])):
                num = str(i)
                responses.append(data['response-' + num])

            submit_test_response(name_or_id, student_name_or_id, responses)

        return redirect('/app?page=exam_list')

    @flaskapp.route("/set_test_case_outputs", methods = ["POST", "GET"])
    def setTestCaseOutputs():
        data = request.values
        if 'name_or_id'in data and 'student_name_or_id' in data and \
            'test_case_outputs' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name']
            test_case_outputs = data['test_case_outputs']
            set_test_case_outputs(name_or_id, student_name_or_id, test_case_outputs)

        return redirect('/app?page=take_exam')

#get test id
def getTestID(name):
    return get_test_id(name)

#does test exist
def doesTestExist(name):
    return does_test_exist(name)

#does test contain question
def doesTestContainQuestion(test_id, question_id):
    return does_test_contain_question(test_id, question_id)

#get questions and points
def getQuestionsAndPoints(name_or_id):
    return get_questions_and_points(name_or_id)

#can delete test
def canDeleteTest(name):
    return can_delete_test(name)

#get user id
def getUserID(username):
    return get_user_id(username)

#get test responses
def getTestResponses(name_or_id, student_name_or_id):
    return get_test_responses(name_or_id, student_name_or_id)

#get test comments
def getTestComments(name_or_id, student_name_or_id):
    return get_test_comments(name_or_id, student_name_or_id)

#get test manual grades
def getTestManualGrades(name_or_id, student_name_or_id):
    return get_test_manual_grades(name_or_id, student_name_or_id)

#get test grades released
def getTestGradesReleased(name_or_id, student_name_or_id):
    return get_test_grades_released(name_or_id, student_name_or_id)

#get test auto grades
def getTestAutoGrades(name_or_id, student_name_or_id):
    return get_test_auto_grades(name_or_id, student_name_or_id)

#get test ids
def getTestIDS():
    return get_test_ids()

#get test names
def getTestNames():
    return get_test_names()

#get_all_responses
def getAllResponses():
    return get_all_responses()

#get test case outputs
def getTestCaseOutputs(name_or_id, student_name_or_id):
    return get_test_case_outputs(name_or_id, student_name_or_id)


def getquestionsintest(id):
    question_ids, point_values = get_questions_and_points(id)
    questions = []

    if question_ids == None:
        question_ids = []

    for i in range (len(question_ids)):
        question_info = get_question(question_ids[i])
        question_info['points'] = point_values[i]
        questions.append(question_info)

    return questions

def getQuestionNotInTest(id):
    questions = get_all_questions()
    exam_questions,_ = get_questions_and_points(id)
    exam_questions = exam_questions or []
    return [question for question in questions if question['id'] not in exam_questions]

def get_names_from_ids():
    test_ids, student_ids = get_all_responses()
    names = []

    for i in range(len(test_ids)):
        testInfo = {"name": get_test_name(test_ids[i]), "student": get_username(student_ids[i])}
        names.append(testInfo)

    return names

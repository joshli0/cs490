import flask
from ..backend.tests import *

def send(app):

    #get test case outputs
    @app.route('/get_test_case_outputs', methods = ('GET', 'POST'))
    def getTestCaseOUtputs():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            return get_test_case_outputs(name_or_id, student_name_or_id)

    #create test
    @app.route('/create_test', methods = ('GET', 'POST'))
    def createTest():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            return create_test(name)

    #add question
    @app.route('/add_question', methods = ('GET', 'POST'))
    def addQuestion():
        data = flask.request.values
        if 'test_id' in data and 'question_id' in data and \
            'point_value' in data:

            test_id = data['test_id']
            question_id = data['question_id']
            point_value = data['point_value']

            return add_question(test_id, question_id, point_value)

    #remove question
    @app.route('/remove_question', methods = ('GET', 'POST'))
    def removeQuestion():
        data = flask.request.values
        if 'test_id' in data and 'question_id' in data:
            test_id = data['test_id']
            question_id = data['question_id']

            return remove_question(test_id, question_id)

    #delete test
    @app.route('/delete_test', methods = ('GET', 'POST'))
    def deleteTest():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            return delete_test(name)

    #submit test responses
    @app.route('/submit_test_response', methods = ('GET', 'POST'))
    def submitTestResponse():
        data = flask.request.values
        if 'name_or_id' in data and 'username' in data and \
            'responses' in data:

            name_or_id = data['name_or_id']
            username = data['username']
            responses = data['responses']

            return submit_test_response(name_or_id, username, responses)

#set test comments
def setTestComments(name_or_id, student_name, comments_on_questions, comments_on_whole_test):
        return set_test_comments(name_or_id, student_name, comments_on_questions, comments_on_whole_test)

#set manual grades
def setTestManualGrades(name_or_id, student_name, manual_grades):
        return set_test_manual_grades(name_or_id, student_name, manual_grades)

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

#submit test response
def submitTestResponse(name_or_id, student_name_or_id, responses):
        return submit_test_response(name_or_id, student_name_or_id, responses)

#get test responses
def getTestResponses(name_or_id, student_name_or_id):
        return get_test_responses(name_or_id, student_name_or_id)

#get test comments
def getTestComments(name_or_id, student_name_or_id):
        return get_test_comments(name_or_id, student_name_or_id)

#set test manual grades
def setTestManualGrades(name_or_id, student_name_or_id, manual_grades):
        return set_test_manual_grades(name_or_id, student_name_or_id, manual_grades)

#get test manual grades
def getTestManualGrades(name_or_id, student_name_or_id):
        return get_test_manual_grades(name_or_id, student_name_or_id)

#set test grades released
def setTestGradesReleased(name_or_id, student_name_or_id, released):
        return set_test_grades_released(name_or_id, student_name_or_id, released)

#get test grades released
def getTestGradesReleased(name_or_id, student_name_or_id):
        return get_test_grades_released(name_or_id, student_name_or_id)

#set test auto grades
def setTestAutoGrades(name_or_id, student_name_or_id, auto_grades):
        return set_test_auto_grades(name_or_id, student_name_or_id, auto_grades)

#get test auto grades
def getTestAutoGrades(name_or_id, student_name_or_id):
        get_test_auto_grades(name_or_id, student_name_or_id)

#set test case outputs
def setTestCaseOutputs(name_or_id, student_name_or_id, test_case_outputs):
        return set_test_case_outputs(name_or_id, student_name_or_id, test_case_outputs)

#get test ids
def getTestIDS():
    return get_test_ids()

#get test names
def getTestNames():
    return get_test_names()
    
#get_all_responses
def getAllResponses():
    return get_all_responses()


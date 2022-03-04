import flask
from ..backend.tests import *

def send(app):

    #create test
    @app.route('/create_test', methods = ('GET', 'POST'))
    def createTest():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            create_test(name)

    #add question
    @app.route('/add_question', methods = ('GET', 'POST'))
    def addQuestion():
        data = flask.request.values
        if 'test_id' in data and 'question_id' in data and \
            'point_value' in data:

            test_id = data['test_id']
            question_id = data['question_id']
            point_value = data['point_value']

            add_question(test_id, question_id, point_value)

    #remove question
    @app.route('/remove_question', methods = ('GET', 'POST'))
    def removeQuestion():
        data = flask.request.values
        if 'test_id' in data and 'question_id' in data:
            test_id = data['test_id']
            question_id = data['question_id']

            remove_question(test_id, question_id)

    #delete test
    @app.route('/delete_test', methods = ('GET', 'POST'))
    def deleteTest():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            delete_test(name)

    #submit test responses
    @app.route('/submit_test_response', methods = ('GET', 'POST'))
    def submitTestResponse():
        data = flask.request.values
        if 'name_or_id' in data and 'username' in data and \
            'responses' in data:

            name_or_id = data['name_or_id']
            username = data['username']
            responses = data['responses']

            submit_test_response(name_or_id, username, responses)
    
    #set test comments
    @app.route('/set_test_comments', methods = ('GET', 'POST'))
    def setTestComments():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name' in data and \
            'comments_on_questions' in data and 'comments_on_whole_test' in data:

            name_or_id = data['name_or_id']
            student_name = data['student_name']
            comments_on_questions = data['comments_on_questions']
            comments_on_whole_test = data['comments_on_whole_test']

            set_test_comments(name_or_id, student_name, comments_on_questions, comments_on_whole_test)
    
    #set manual grades
    @app.route('/set_test_manual_grades', methods = ('GET', 'POST'))
    def setTestManualGrades():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name' in data and \
            'manual_grades' in data:

            name_or_id = data['name_or_id']
            student_name = data['student_name']
            manual_grades = data['manual_grades']

            set_test_manual_grades(name_or_id, student_name, manual_grades)

    #get test ids
    @app.route('/get_test_ids', methods = ('GET', 'POST'))
    def getTestIDS():
        get_test_ids()

    #get test names
    @app.route('/get_test_names', methods = ('GET', 'POST'))
    def getTestNames():
        get_test_names()
    
    #get test id
    @app.route('/get_test_id', methods = ('GET', 'POST'))
    def getTestID():
        data = flask.request.values
        if 'name' in data:
            name = data['name']
            get_test_id(name)
    
    #does test exist
    @app.route('/does_test_exist', methods = ('GET', 'POST'))
    def doesTestExist():
        data = flask.request.values
        if 'name' in data:
            name = data['name']
            does_test_exist(name)   

    #does test contain question
    @app.route('/does_test_contain_question', methods = ('GET', 'POST'))
    def doesTestContainQuestion():
        data = flask.request.values
        if 'test_id' in data and 'question_id' in data:
            test_id = data['test_id']
            question_id = data['question_id']
            does_test_contain_question(test_id, question_id)

    #get questions and points
    @app.route('/get_questions_and_points', methods = ('GET', 'POST'))
    def getQuestionsAndPoints():
        data = flask.request.values
        if 'name_or_id' in data:
            name_or_id = data['name_or_id']
            get_questions_and_points(name_or_id)

    #can delete test
    @app.route('/can delete test', methods = ('GET', 'POST'))
    def canDeleteTest():
        data = flask.request.values
        if 'name' in data:
            name = data['name']
            can_delete_test(name)

    #get user id
    @app.route('/get_user_id', methods = ('GET', 'POST'))
    def getUserID():
        data = flask.request.values
        if 'username' in data:
            username = data['username']
            get_user_id(username)

    #get_all_responses
    @app.route('/get_all_responses', methods = ('GET', 'POST'))
    def getAllResponses():
        get_all_responses()

    #submit test response
    @app.route('/submit_test_response', methods = ('GET', 'POST'))
    def submitTestResponse():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data and \
            'responses' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            responses = data['responses']
            submit_test_response(name_or_id, student_name_or_id, responses)
    
    #get test responses
    @app.route('/get_test_responses', methods = ('GET', 'POST'))
    def getTestResponses():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            get_test_responses(name_or_id, student_name_or_id)

    #get test comments
    @app.route('/get_test_comments', methods = ('GET', 'POST'))
    def getTestComments():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            get_test_comments(name_or_id, student_name_or_id)

    #set test manual grades
    @app.route('/set_test_manual_grades', methods = ('GET', 'POST'))
    def setTestManualGrades():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data and \
            'manual_grades' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            manual_grades = data['manual_grades']
            set_test_manual_grades(name_or_id, student_name_or_id, manual_grades)

    #get test manual grades
    @app.route('/get_test_manual_grades', methods = ('GET', 'POST'))
    def getTestManualGrades():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            get_test_manual_grades(name_or_id, student_name_or_id)

    #set test grades released
    @app.route('/set_test_grades_released', methods = ('GET', 'POST'))
    def setTestGradesReleased():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data and \
            'released' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            released = data['released']
            set_test_grades_released(name_or_id, student_name_or_id, released)

    #get test grades released
    @app.route('/get_test_grades_released', methods = ('GET', 'POST'))
    def getTestGradesReleased():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            get_test_grades_released(name_or_id, student_name_or_id)

    #set test auto grades
    @app.route('/set_test_auto_grades', methods = ('GET', 'POST'))
    def setTestAutoGrades():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data and \
            'auto_grades' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            auto_grades = data['auto_grades']
            set_test_auto_grades(name_or_id, student_name_or_id, auto_grades)

    #get test auto grades
    @app.route('/get_test_auto_grades', methods = ('GET', 'POST'))
    def getTestAutoGrades():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            get_test_auto_grades(name_or_id, student_name_or_id)

    #set test case outputs
    @app.route('/set_test_case_outputs', methods = ('GET', 'POST'))
    def setTestCaseOutputs():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data and \
            'test_case_outputs' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            test_case_outputs = data['test_case_outputs']
            set_test_case_outputs(name_or_id, student_name_or_id, test_case_outputs)

    #get test case outputs
    @app.route('/get_test_case_outputs', methods = ('GET', 'POST'))
    def getTestCaseOUtputs():
        data = flask.request.values
        if 'name_or_id' in data and 'student_name_or_id' in data:
            name_or_id = data['name_or_id']
            student_name_or_id = data['student_name_or_id']
            get_test_case_outputs(name_or_id, student_name_or_id)
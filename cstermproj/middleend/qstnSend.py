import flask
from ..backend.questions import *

def send(app):
    #create question
    @app.route('/create_question', methods = ('GET', 'POST'))
    def createQuestion():
        data = flask.request.values
        if 'title' in data and 'description' in data and \
            'difficulty' in data and 'category' in data and \
            'function_name' in data and 'test_case_args' in data and \
            'test_case_results' in data:

            title = data['title']
            description = data['description']
            difficulty = data['difficulty']
            category = data['category']
            function_name = data['function_name']
            test_case_args = data['test_case_args']
            test_case_results = data['test_case_results']

            return create_question(title, description, difficulty, category,
            function_name, test_case_args, test_case_results)

    #edit question
    @app.route('/edit_question', methods = ('GET', 'POST'))
    def editQuestion():
        data = flask.request.values
        if 'id' in data and 'title' in data and \
            'description' in data and 'difficulty' in data and \
            'category' in data and 'function_name' in data and \
            'test_case_args' in data and 'test_case_results' in data:

            id = data['id']
            title = data['title']
            description = data['description']
            difficulty = data['difficulty']
            category = data['category']
            function_name = data['function_name']
            test_case_args = data['test_case_args']
            test_case_results = data['test_case_results']

            return edit_question(id, title, description, difficulty, category,
            function_name, test_case_args, test_case_results)

    #delete question
    @app.route('/delete_question', methods = ('GET', 'POST'))
    def deleteQuestion():
        data = flask.request.values
        if 'id' in data:
            id = data['id']

            return delete_question(id)

    #add difficulty
    @app.route('/add_difficulty', methods = ('GET', 'POST'))
    def addDifficulty():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            return add_difficulty(name)

    #delete difficulty
    @app.route('/delete_difficulty', methods = ('GET', 'POST'))
    def deleteDifficulty():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            return delete_difficulty(name)

    #rename difficulty
    @app.route('/rename_difficulty', methods = ('GET', 'POST'))
    def renameDifficulty():
        data = flask.request.values
        if 'old_name' in data and 'new_name' in data:
            old_name = data['old_name']
            new_name = data['new_name']

            return rename_difficulty(old_name, new_name)

    #add category
    @app.route('/add_category', methods = ('GET', 'POST'))
    def addCategory():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            return add_category(name)

    #delete category
    @app.route('/delete_category', methods = ('GET', 'POST'))
    def deleteCategory():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            return delete_category(name)

    #rename category
    @app.route('/rename_category', methods = ('GET', 'POST'))
    def renameCategory():
        data = flask.request.values
        if 'old_name' in data and 'new_name' in data:
            old_name = data['old_name']
            new_name = data['new_name']

            return rename_category(old_name, new_name)

#can delete difficulty
def canDeleteDiff(name):
        return can_delete_difficulty(name)

#can delete category
def canDeleteCat(name):
        return can_delete_category(name)

#does question exist
def doesQuestionExist(id):
        return does_question_exist(id)

#get question
def getQuestion(id):
        return get_question(id)

#get question function name
def getQuestionFunctionName(id):
        return get_question_function_name(id)

#get question test cases
def getQuestionTestCases(id):
        return get_question_test_cases(id)

#can delete question
def canDeleteQuestion(id):
        return can_delete_question(id)

#get question difficulties
def getDiff():
    return get_difficulties()

#get question categories
def getCat():
    return get_categories()

#get question ids
def getQuestionIDS():
    return get_question_ids()

#get question titles
def getQuestionTitles():
    return get_question_titles()

#get all questions
def getAllQuestions():
    return get_all_questions()
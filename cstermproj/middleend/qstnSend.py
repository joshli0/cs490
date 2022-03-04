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

            create_question(title, description, difficulty, category,
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

            edit_question(id, title, description, difficulty, category,
            function_name, test_case_args, test_case_results)

    #delete question
    @app.route('/delete_question', methods = ('GET', 'POST'))
    def deleteQuestion():
        data = flask.request.values
        if 'id' in data:
            id = data['id']

            delete_question(id)

    #add difficulty
    @app.route('/add_difficulty', methods = ('GET', 'POST'))
    def addDifficulty():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            add_difficulty(name)

    #delete difficulty
    @app.route('/delete_difficulty', methods = ('GET', 'POST'))
    def deleteDifficulty():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            delete_difficulty(name)

    #rename difficulty
    @app.route('/rename_difficulty', methods = ('GET', 'POST'))
    def renameDifficulty():
        data = flask.request.values
        if 'old_name' in data and 'new_name' in data:
            old_name = data['old_name']
            new_name = data['new_name']

            rename_difficulty(old_name, new_name)

    #add category
    @app.route('/add_category', methods = ('GET', 'POST'))
    def addCategory():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            add_difficulty(name)

    #delete category
    @app.route('/delete_category', methods = ('GET', 'POST'))
    def deleteCategory():
        data = flask.request.values
        if 'name' in data:
            name = data['name']

            delete_category(name)

    #rename category
    @app.route('/rename_category', methods = ('GET', 'POST'))
    def renameCategory():
        data = flask.request.values
        if 'old_name' in data and 'new_name' in data:
            old_name = data['old_name']
            new_name = data['new_name']

            rename_category(old_name, new_name)

    #get difficulty
    @app.route('/get_difficulty', methods = ('GET', 'POST'))
    def getDiff():
        get_difficulties()

    #can delete difficulty
    @app.route('/can_delete_difficulty', methods = ('GET', 'POST'))
    def canDeleteDiff():
        data = flask.request.values
        if 'name' in data:
            name = data['name']
            can_delete_difficulty(name)

    #get categories
    @app.route('/get_categories', methods = ('GET', 'POST'))
    def getCat():
        get_categories()

    #can delete category
    @app.route('/can_delete_category', methods = ('GET', 'POST'))
    def canDeleteCat():
        data = flask.request.values
        if 'name' in data:
            name = data['name']
            can_delete_category(name)

    #get question ids
    @app.route('/get_question_ids', methods = ('GET', 'POST'))
    def getQuestionIDS():
        get_question_ids()
    
    #does question exist
    @app.route('/does_question_exist', methods = ('GET', 'POST'))
    def doesQuestionExist():
        data = flask.request.values
        if 'id' in data:
            id = data['id']
            does_question_exist(id)
    
    #get question titles
    @app.route('/get_question_titles', methods = ('GET', 'POST'))
    def getQuestionTitles():
        get_question_titles()
    
    #get question
    @app.route('/get_question', methods = ('GET', 'POST'))
    def getQuestion():
        data = flask.request.values
        if 'id' in data:
            id = data['id']
            get_question(id)

    #get question function name
    @app.route('/get_question_function_name', methods = ('GET', 'POST'))
    def getQuestionFunctionName():
        data = flask.request.values
        if 'id' in data:
            id = data['id']
            get_question_function_name(id)

    #get question test cases
    @app.route('/get_question_test_cases', methods = ('GET', 'POST'))
    def getQuestionTestCases():
        data = flask.request.values
        if 'id' in data:
            id = data['id']
            get_question_test_cases(id)

    #can delete question
    @app.route('/can_delete_question', methods = ('GET', 'POST'))
    def canDeleteQuestion():
        data = flask.request.values
        if 'id' in data:
            id = data['id']
            can_delete_question(id)
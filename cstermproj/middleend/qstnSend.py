import flask
from flask import Flask, request, redirect
from ..backend.questions import *

#create question
def send(flaskapp):
    @flaskapp.route("/create_question", methods = ["POST", "GET"])
    def createQuestion():
        data = request.values
        if 'title' in data and 'description' in data and 'difficulty' in data \
            and 'category' in data and 'function_name' in data \
            and 'test_case_args' in data and 'test_case_results' in data:
            title = data['title']
            description = data['description']
            difficulty = data['difficulty']
            category = data['category']
            function_name = data['function_name']
            test_case_args = data['test_case_args']
            test_case_results = data['test_case_results']

            create_question(title, description, difficulty, category, function_name, test_case_args, test_case_results)
        
        return redirect('/app?page=manage_questions')
    
    @flaskapp.route("/edit_question", methods = ["POST", "GET"])
    def editQuestion():
        data = request.values
        if 'id' in data and 'title' in data and 'description' in data and 'difficulty' in data \
            and 'category' in data and 'function_name' in data \
            and 'test_case_args' in data and 'test_case_results' in data:
            id = data['id']
            title = data['title']
            description = data['description']
            difficulty = data['difficulty']
            category = data['category']
            function_name = data['function_name']
            test_case_args = data['test_case_args']
            test_case_results = data['test_case_results']

            edit_question(id, title, description, difficulty, category, function_name, test_case_args, test_case_results)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/delete_question", methods = ["POST", "GET", "DELETE"])
    def deleteQuestion():
        data = request.values
        if 'id' in data:
            id = data['id']
            delete_question(id)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/add_difficulty", methods = ["POST", "GET"])
    def addDifficulty():
        data = request.values
        if 'name' in data:
            name = data['name']
            add_difficulty(name)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/delete_difficulty", methods = ["POST", "GET", "DELETE"])
    def deleteDifficulty():
        data = request.values
        if 'name' in data:
            name = data['name']
            delete_difficulty(name)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/rename_difficulty", methods = ["POST", "GET"])
    def renameDifficulty():
        data = request.values
        if 'old_name' in data and 'new_name' in data:
            old_name = data['old_name']
            new_name = data['new_name']
            add_difficulty(old_name, new_name)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/add_category", methods = ["POST", "GET"])
    def addCategory():
        data = request.values
        if 'name' in data:
            name = data['name']
            add_category(name)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/delete_category", methods = ["POST", "GET", "DELETE"])
    def deleteCategory():
        data = request.values
        if 'name' in data:
            name = data['name']
            delete_category(name)
        
        return redirect('/app?page=manage_questions')

    @flaskapp.route("/rename_category", methods = ["POST", "GET"])
    def renameCategory():
        data = request.values
        if 'old_name' in data and 'new_name' in data:
            old_name = data['old_name']
            new_name = data['new_name']
            rename_category(old_name, new_name)
        
        return redirect('/app?page=manage_questions')

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
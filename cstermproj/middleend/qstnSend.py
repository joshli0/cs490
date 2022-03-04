import flask
from ..backend.questions import *

#create question
def createQuestion(title, description, difficulty, category, function_name, test_case_args, test_case_results):
    return create_question(title, description, difficulty, category, function_name, test_case_args, test_case_results)

#edit question
def editQuestion(id, title, description, difficulty, category, function_name, test_case_args, test_case_results):
    return edit_question(id, title, description, difficulty, category, function_name, test_case_args, test_case_results)

#delete question
def deleteQuestion(id):
    return delete_question(id)

#add difficulty
def addDifficulty(name):
    return add_difficulty(name)

#delete difficulty
def deleteDifficulty(name):
    return delete_difficulty(name)

#rename difficulty
def renameDifficulty(old_name, new_name):
     return rename_difficulty(old_name, new_name)

#add category
def addCategory(name):
    return add_category(name)

#delete category
def deleteCategory(name):
    return delete_category(name)

#rename category
def renameCategory(old_name, new_name):
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
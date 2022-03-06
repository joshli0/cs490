import flask

from ..backend.autograder import *

def send(flaskapp):
    @flaskapp.route('/autograde', methods = ['POST', 'GET'])
    def runAutoGraderOnEverything():
        run_auto_grader_on_everything()
        return flask.redirect('/app?page=manage_exams')
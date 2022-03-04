import flask

from ..backend.autograder import *

def send(app):
    @app.route('/run_auto_grader_on_everything', methods = ('GET', 'POST'))
    def runAutoGraderOnEverything():
        return run_auto_grader_on_everything()

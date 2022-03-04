import flask

from ..backend.autograder import *

def send(app):
    @app.route('/run_auto_grader_on_everything', methods = ('GET', 'POST'))
    def runAutoGraderOnEverything():
        run_auto_grader_on_everything()

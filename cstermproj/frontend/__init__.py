import flask
from .login import setup as setup_login
from .landing import landing
from .manage_questions import manage_questions
from .manage_exams import manage_exams
from .grade_exams import grade_exams

def startup(flaskapp):
	setup_login(flaskapp)

	@flaskapp.route("/app", methods = ["GET"])
	def app():

		args = flask.request.args

		if "page" in args:
			page = args["page"]
		else:
			page = "landing"

		if page == "landing":
			return landing()
		elif page == "manage_questions":
			return manage_questions()
		elif page == "manage_exams":
			return manage_exams()
		elif page == "grade_exams":
			return grade_exams()
		else:
			return flask.redirect("/app")

		return landing()

import flask
from .login import setup as setup_login
from .landing import landing
from .nav import *

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

		if flask.session["teacher"]:
			if page == "manage_questions":
				return manage_questions()
			elif page == "manage_exams":
				return manage_exams()
			elif page == "build_exam":
				return build_exam()
			elif page == "grade_exams":
				return grade_exams()
			elif page == "review_exam":
				return review_exam()
		else:
			if page == "exam_list":
				return exam_list()
			elif page == "view_results":
				return view_results()
			elif page == "take_exam":
				return take_exam()
			elif page == "results":
				return results()

		return flask.redirect("/app")

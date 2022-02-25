import flask

def teacher_landing():
	return flask.render_template("teacher_landing.html")

def student_landing():
	return flask.render_template("student_landing.html")

def landing():
	if flask.session["teacher"]:
		return teacher_landing()
	else:
		return student_landing()
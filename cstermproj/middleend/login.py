import flask

from ..backend.login import check_credentials

def setup(flaskapp):
	@flaskapp.before_request
	def check_logged_in():
		url = flask.request.path.lower()
		
		if "user" in flask.session:
			if url == "/login":
				return flask.redirect("/app")
		elif url not in ["/login", "/style.css", "/favicon.ico"]:
			return flask.redirect("/login")
	
	@flaskapp.route("/login", methods = ["POST"])
	def login_process():
		data = flask.request.values
		success = False
		
		if "username" in data and "password" in data:
			username = data["username"]
			password = data["password"]
			
			if username is not None and len(username) > 0 and password is not None and len(password) > 0:
				teacher_or_student = check_credentials(username, password)
				
				if teacher_or_student is not None:
					flask.session["user"] = username
					flask.session["teacher"] = teacher_or_student
					
					success = True
		
		flask.session["errmsg"] = None if success else "Invalid username or password!"
		return flask.redirect("/app" if success else "/login")
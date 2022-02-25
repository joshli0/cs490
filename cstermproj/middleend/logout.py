import flask

def setup(flaskapp):
	@flaskapp.route("/logout")
	def logout():
		flask.session.clear()
		return flask.redirect("/login")
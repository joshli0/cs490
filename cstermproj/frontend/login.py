import flask

def setup(flaskapp):
	@flaskapp.route("/")
	def index():
		return flask.redirect("/login")
	
	@flaskapp.route("/login", methods = ["GET"])
	def login():
		return flask.render_template("index.html")
		flask.session["errmsg"] = None
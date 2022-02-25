from .login import setup as setup_login
from .landing import landing

def startup(flaskapp):
	setup_login(flaskapp)
	
	@flaskapp.route("/app", methods = ["GET"])
	def app():
		return landing()
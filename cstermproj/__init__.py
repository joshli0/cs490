from secrets import token_urlsafe

from flask import Flask

from .frontend  import startup as start_front
from .middleend import startup as start_middle
from .backend   import startup as start_back

def startup():
	flaskapp = Flask(
		__name__,
		static_url_path = "/",
		static_folder   = "../static/",
		template_folder = "../templates/"
	)
	
	flaskapp.secret_key = token_urlsafe(16)
	
	start_front(flaskapp)
	start_middle(flaskapp)
	start_back()
	
	return flaskapp
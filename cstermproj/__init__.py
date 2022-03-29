from secrets import token_urlsafe

from flask import Flask
from flask_session import Session

from .frontend  import startup as start_front
from .middleend import startup as start_middle
from .backend   import startup as start_back

from .backend.dbconn import get_environment_var, get_db_uri

def startup():
	flaskapp = Flask(
		__name__,
		static_url_path = "/",
		static_folder   = "../static/",
		template_folder = "../templates/"
	)
	
	key = get_environment_var("SESSION_SECRET_KEY")
	if key is None:
		print("Warning: Generating RANDOM session key, this WILL NOT WORK in production!")
		key = token_urlsafe(16)
	flaskapp.secret_key = key
	
	start_back()
	
	flaskapp.config["SESSION_TYPE"] = "sqlalchemy"
	flaskapp.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"
	flaskapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	flaskapp.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri().replace("postgres", "postgresql+psycopg2")
	
	s = Session(flaskapp)
	s.app.session_interface.db.create_all()
	
	start_middle(flaskapp)
	start_front(flaskapp)
	
	return flaskapp
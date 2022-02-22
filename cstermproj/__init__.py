from flask import Flask
flaskapp = Flask(__name__)

from .backend.database_interface import con

@flaskapp.route("/")
def index():
	cur = con.cursor()
	cur.execute("SELECT sqrt(2);")
	
	body = "extremely simple test<br>" + str(cur.fetchall())
	return "<html><head><title>howdy</title></head><body>" + body + "</body></html>"
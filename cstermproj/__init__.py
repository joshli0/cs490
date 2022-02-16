from flask import Flask
flaskapp = Flask(__name__)

@flaskapp.route("/")
def index():
	return "<html><head><title>howdy</title></head><body>extremely simple test</body></html>"
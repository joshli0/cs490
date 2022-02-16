from flask import Flask
flaskapp = Flask(__name__)

@app.route("/")
def index():
	return "<html><head><title>howdy</title></head><body>extremely simple test</body></html>"
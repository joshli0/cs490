from .dbconn import connect as connect_to_db

def startup():
	connect_to_db()
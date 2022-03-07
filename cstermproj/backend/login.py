import hashlib

from .dbconn import query

def sha256(text):
	return hashlib.sha256(text.encode("utf8")).hexdigest()

def check_credentials(username, password):
	results = query("select AccessType from CS490Proj.Users where Username = %s and PassHash = %s", (username, sha256(password)))
	
	if results is not None and len(results) == 1:
		return results[0][0] == "Teacher"

def get_username(id):
	results = query("select Username from CS490Proj.Users where ID = %s", (id, ))
	
	if results is not None and len(results) == 1:
		return results[0][0]
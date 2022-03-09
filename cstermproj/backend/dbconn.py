import os

import psycopg2
import psycopg2.extras

uri = None
con = None

def get_environment_var(name):
	return os.environ[name] if name in os.environ else None

def connect():
	global uri, con
	uri = get_environment_var("DATABASE_URL")
	con = psycopg2.connect(uri, sslmode = "require")

def get_db_uri():
	return uri

def query(query, *args, as_dict = False):
	cur_params = {}
	
	if as_dict:
		cur_params["cursor_factory"] = psycopg2.extras.RealDictCursor
	
	cur = con.cursor(**cur_params)
	cur.execute(query, *args)
	
	try:
		res = cur.fetchall()
	except psycopg2.ProgrammingError:
		res = None
	
	if as_dict and res is not None:
		res = [dict(r) for r in res]
	
	cur.close()
	return res

def commit():
	con.commit()
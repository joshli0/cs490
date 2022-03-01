import os
import psycopg2

con = None

def connect():
	global con
	con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode = "require")

def query(query, *args):
	cur = con.cursor()
	
	cur.execute(query, *args)
	res = cur.fetchall()
	
	cur.close()
	return res
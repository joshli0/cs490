from . import startup
flaskapp = startup()

if __name__ == "__main__":
	flaskapp.run(threaded = True)
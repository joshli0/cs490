from .login  import setup as setup_login
from .logout import setup as setup_logout

def startup(flaskapp):
	setup_login (flaskapp)
	setup_logout(flaskapp)
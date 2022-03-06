from .login  import setup as setup_login
from .logout import setup as setup_logout
from .qstnSend import send as setup_qstnSend
from .testSend import send as setup_testSend
from .autoSend import runAutoGraderOnEverything as setup_autoSend

def startup(flaskapp):
	setup_login (flaskapp)
	setup_logout(flaskapp)
	setup_qstnSend(flaskapp)
	setup_testSend(flaskapp)
	setup_autoSend()
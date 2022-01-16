from pyScripts.main import ind
from pyScripts.italiano import ita
from pyScripts.login import log
from pyScripts.users import use

from flask import Flask, sessions

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(ind)
app.register_blueprint(ita)
app.register_blueprint(log)
app.register_blueprint(use)

session_cookie = sessions.SecureCookieSessionInterface().get_cookie_secure(app)

if __name__ == '__main__':
    app.run()

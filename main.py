from pyScripts.verbItaliano.main import verbInd
from pyScripts.verbItaliano.italiano import verbIta
from pyScripts.verbItaliano.login import verbLog
from pyScripts.verbItaliano.users import verbUse

from pyScripts.raphaelCordon.main import rcMain


from flask import Flask, sessions

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(verbInd)
app.register_blueprint(verbIta)
app.register_blueprint(verbLog)
app.register_blueprint(verbUse)

app.register_blueprint(rcMain)

session_cookie = sessions.SecureCookieSessionInterface().get_cookie_secure(app)

if __name__ == '__main__':
    app.run(debug=True)

from passlib.hash import sha256_crypt
from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.verbItaliano.authentication import AuthenticateRepository


verbLog = Blueprint('verbLog', __name__)


@verbLog.route('/login')
def login():

    return render_template('verbItaliano/account/login.html')


@verbLog.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
    # <- Check Email ->
    session['email'] = request.form['email']
    if AuthenticateRepository().auth(
            str(request.form['email']).lower().strip()):
        user = AuthenticateRepository().auth(
            str(request.form['email']).lower().strip())
    else:
        flash('Verifique e-Mail e/ou senha e tente novamente', 'danger')
        return redirect(url_for('log.login'))

    # <- Check Password ->
    password = request.form['password']
    isValidPass = sha256_crypt.verify(password, user.password)

    if isValidPass:
        if user.changepass:
            return redirect(url_for('use.changePass'))
        else:
            UpdateSession(user)
            flash(f'Bem vindo {user.name}', 'success')

            return redirect(url_for('ind.adm'))
    else:
        flash('Verifique usuário e/ou senha e tente novamente', 'danger')
        return redirect(url_for('log.login'))


@verbLog.route('/logout')
def logout():
    """
    :return: Cleaning Session
    """
    session['id'] = ''
    session['name'] = ''
    session['email'] = ''
    session['surname'] = ''

    return redirect(url_for('ind.adm'))


@verbLog.route('/newAccount')
def newAccount():
    return render_template('verbItaliano/account/newAccount.html')


def UpdateSession(user):
    """
    :param user: list info from user from db
    :return: Session populated with current user's info
    id / name / surname / password (encripted)
    """
    session['id'] = user.id
    session['email'] = user.email
    session['name'] = user.name
    session['surname'] = user.surname
    session['password'] = user.password

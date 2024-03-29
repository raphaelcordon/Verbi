from flask import redirect, request, url_for, flash, Blueprint, session, render_template
from pyScripts.verbItaliano.login import UpdateSession
from passlib.hash import sha256_crypt
from thirdparty.verbItaliano.gmail import EmailPassword
import random
import string
from repository.verbItaliano.users import UsersRepository

verbUse = Blueprint('verbUse', __name__)


@verbUse.route('/UsersRegistry', methods=['POST', ])
def UsersRegistry():
    name = str(request.form['name']).strip().title()
    surname = str(request.form['surname']).strip().title()
    email = str(request.form['email']).strip().lower()

    session['name'] = name
    session['surname'] = surname
    session['email'] = email

    if request.form['password1'] == request.form['password2'] and len(str(request.form['password1'])) >= 5:
        password = sha256_crypt.hash(str(request.form['password1']))
    else:
        flash("Os critérios para criação de senha não foram respeitados.", 'warning')
        return redirect(url_for('log.newAccount'))

    if UsersRepository().FindByEmail(email):
        flash('E-Mail já cadastrado, tente outro', 'info')
        return redirect(url_for('log.newAccount'))
    else:
        UsersRepository().New(name, surname, password, email)
        if UsersRepository().FindByEmail(email):
            flash("Usuário criado com sucesso.", 'success')
        else:
            flash("Algo deu errado, por favor, tente novamente", 'danger')
        return redirect(url_for('log.login'))


@verbUse.route('/editAccount')
def editAccount():
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('ind.adm'))
    else:

        return render_template('verbItaliano/account/editAccount.html', user=UsersRepository().FindById(session['id']))


@verbUse.route('/updateAccountDb', methods=['POST', 'GET'])
def updateAccountDb():
    UsersRepository().Update(
        request.form['id'],
        request.form['name'],
        request.form['surname'],
        request.form['email']
    )

    session['name'] = request.form['name']
    session['surname'] = request.form['surname']
    session['email'] = request.form['email']

    flash('Dados atualizados com sucesso', 'success')
    return redirect(url_for('use.editAccount'))

#  <---- defs related to PASSWORD beginning ---->


@verbUse.route('/changePass')
def changePass():
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))
    else:
        return render_template('verbItaliano/account/changePass.html', data=id)


@verbUse.route('/updatePassDb', methods=['POST', 'GET'])
def updatePassDb():
    try:
        user = UsersRepository().FindByEmail(request.form['email'])
        if user.email and sha256_crypt.verify(request.form['passwordOld'], user.password):
            if request.form['password1'] == request.form['password2']:
                password = sha256_crypt.hash(str(request.form['password1']))
                UsersRepository().UpdatePassword(user.id, password)
                UpdateSession(user)
                flash('Senha alterada com sucesso', 'success')
                return redirect(url_for('ind.adm'))
            else:
                flash('As novas senhas não são identicas, tente novamente', 'danger')
                return redirect(url_for('use.changePass'))
        else:
            flash('e-Mail e/ou senha atual incorretos', 'danger')
            return redirect(url_for('use.changePass'))
    except:
        flash('e-Mail e/ou senha atual incorretos', 'danger')
        return redirect(url_for('use.changePass'))


#  <-- Reset Pass -->

@verbUse.route('/resetPass')
def resetPass():

    return render_template('verbItaliano/account/resetPass.html')


@verbUse.route('/resetEmailPass', methods=['POST', 'GET'])
def resetEmailPass():
    if not UsersRepository().FindByEmail(request.form['email']):
        session['email'] = request.form['email']
        flash('e-Mail não encontrado', 'info')
        return redirect(url_for('use.resetPass'))
    else:
        user = UsersRepository().FindByEmail(request.form['email'])
        tempPass = str(get_random_string())
        UsersRepository().ResetPassword(user.email, sha256_crypt.hash(str(tempPass)))
        EmailPassword(user.email, user.name, tempPass)
        flash("Senha enviada para email o cadastrado", 'success')
        return redirect(url_for('log.login'))


#  <---- defs related to PASSWORD ending ---->

def get_random_string():
    """
    Get temporary password generating random string
    :return: 5 random characters
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))

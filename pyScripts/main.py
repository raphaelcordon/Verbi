from flask import render_template, session, redirect, url_for, Blueprint, Response, request, flash
from repository.verbi_repos import VerbiRepository as VerbiRepo

ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():
    return render_template('index.html')


@ind.route('/adm')
def adm():
    return render_template('adm/adm.html')


@ind.route('/adm/verbiItaliano/', methods=['GET', 'POST'])
def admItaliano():
    verbo = str(request.form['verbo']).lower().strip()
    verbi = VerbiRepo().ListDistinctVerbs()
    if VerbiRepo().FindByVerb(verbo):
        ilverbo = VerbiRepo().FindByVerb(verbo)
        return render_template('adm/italiano.html', verbi=verbi, ilverbo=ilverbo)
    else:
        flash(f'Verbo non trovato, trovane un altro', 'danger')
        return redirect(url_for('ind.adm'))

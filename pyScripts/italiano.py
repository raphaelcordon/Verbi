from flask import render_template, session, redirect, url_for, Blueprint, Response, request
from repository.italiano_repos import ItalianoRepository as Repo
from repository.verbi_repos import VerbiRepository as VerbiRepo
from thirdparty.api import ApiUltralingua

ita = Blueprint('ita', __name__, url_prefix='')


@ita.route('/italianoMain')
def italianoMain():
    verbi = VerbiRepo().ListDistinctVerbs()

    sequence = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z')

    return render_template('italiano/italianoMain.html', verbi=verbi, sequence=sequence)


@ita.route('/italiano/<verbo>/', methods=['GET', 'POST'])
def italianoVerbo(verbo):

    ilverbo = VerbiRepo().FindByVerb(verbo)
    verbi = VerbiRepo().ListDistinctVerbs()

    return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)


@ita.route('/', methods=['GET', 'POST'])
def italianoAltroVerbo():

    verbo = str(request.form['verbo']).lower().strip()
    verbi = VerbiRepo().ListDistinctVerbs()
    tryVerbo = VerbiRepo().FindByVerb(verbo)
    if tryVerbo:
        ilverbo = tryVerbo
    else:
        ApiUltralingua(verbo)
        ilverbo = VerbiRepo().FindByVerb(verbo)

    return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)


@ita.route('/admitaliano')
def admitaliano():

    return render_template('italiano/admitaliano.html')


@ita.route('/', methods=['GET', 'POST'])
def italianoNovoVerbo():

    return render_template('italiano/admitaliano.html')


@ita.route('/testVerbi/', methods=['GET', 'POST'])
def testVerbi():

    verbi = VerbiRepo().List()
    return render_template('italiano/Testitaliano.html', verbi=verbi)

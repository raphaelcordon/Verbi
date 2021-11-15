from flask import render_template, session, redirect, url_for, Blueprint, Response, request
from repository.italiano_repos import ItalianoRepository as Repo

ita = Blueprint('ita', __name__, url_prefix='')


@ita.route('/italianoMain')
def italianoMain():
    verbi = Repo().ListDistinctVerbs()
    sequence = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z')

    return render_template('italiano/italianoMain.html', verbi=verbi, sequence=sequence)


@ita.route('/italiano/<verbo>/', methods=['GET', 'POST'])
def italianoVerbo(verbo):

        verbi = Repo().ListDistinctVerbs()
        ilverbo = Repo().FindByVerb(verbo)

        return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)


@ita.route('/', methods=['GET', 'POST'])
def italianoAltroVerbo():

        verbo = str(request.form['verbo']).lower()
        verbi = Repo().ListDistinctVerbs()
        ilverbo = Repo().FindByVerb(verbo)

        return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)


@ita.route('/admitaliano')
def admitaliano():

    return render_template('italiano/admitaliano.html')


@ita.route('/', methods=['GET', 'POST'])
def italianoNovoVerbo():



        return render_template('italiano/admitaliano.html')
from flask import render_template, Blueprint, request, flash, redirect, url_for
from repository.verbi_repos import VerbiRepository as VerbiRepo
from repository.italianoCondizionale_repos import VerbiRepository as VerbiCondizionale
from thirdparty.api import ApiUltralingua

ita = Blueprint('ita', __name__, url_prefix='')


@ita.route('/italianoMain')
def italianoMain():
    verbi = VerbiRepo().ListDistinctVerbs()

    sequence = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'z')
    top20 = ('essere', 'avere', 'fare', 'dire', 'potere', 'volere', 'sapere', 'stare', 'dovere', 'vedere', 'andare',
             'venire', 'dare', 'parlare', 'trovare', 'sentire', 'lasciare', 'prendere', 'guardare', 'mettere')

    return render_template('italiano/italianoMain.html', verbi=verbi, sequence=sequence, top20=top20)


@ita.route('/italiano/<verbo>/', methods=['GET', 'POST'])
def italianoVerbo(verbo):

    ilverbo = VerbiRepo().FindByVerb(verbo)
    verbi = VerbiRepo().ListDistinctVerbs()
    verbiCondizionale = VerbiCondizionale().FindByVerb(verbo)

    return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo, verbiCondizionale=verbiCondizionale)


@ita.route('/', methods=['GET', 'POST'])
def italianoAltroVerbo():

    verbo = str(request.form['verbo']).lower().strip()
    verbi = VerbiRepo().ListDistinctVerbs()
    if VerbiRepo().FindByVerb(verbo):
        ilverbo = VerbiRepo().FindByVerb(verbo)
        return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)
    else:
        try:
            ApiUltralingua(verbo)
            ilverbo = VerbiRepo().FindByVerb(verbo)
            return render_template('italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)
        except:
            flash(f'Verbo non trovato, trovane un altro', 'danger')
            return redirect(url_for('ita.italianoMain'))

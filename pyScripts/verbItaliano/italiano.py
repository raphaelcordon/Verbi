from flask import render_template, Blueprint, request, flash, redirect, url_for
from repository.verbItaliano.verbi_repos import VerbiRepository as VerbiRepo
from repository.verbItaliano.italianoRiflessivi_repos import VerbiRepository as RiflessiviRepo
from repository.verbItaliano.italianoCondizionale_repos import VerbiRepository as VerbiCondizionale
from thirdparty.verbItaliano.api import ApiUltralingua

verbIta = Blueprint('verbIta', __name__, url_prefix='')


@verbIta.route('/italianoMain')
def italianoMain():
    verbi = VerbiRepo().ListDistinctVerbs()
    riflessivi = RiflessiviRepo().ListDistinctVerbs()

    sequence = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'z')
    top20 = ('essere', 'avere', 'fare', 'dire', 'potere', 'volere', 'sapere', 'stare', 'dovere', 'vedere', 'andare',
             'venire', 'dare', 'parlare', 'trovare', 'sentire', 'lasciare', 'prendere', 'guardare', 'mettere')

    return render_template('verbItaliano/italiano/italianoMain.html', verbi=verbi, riflessivi=riflessivi, sequence=sequence,
                           top20=top20)


@verbIta.route('/italiano/<verbo>/', methods=['GET', 'POST'])
def italianoVerbo(verbo):

    if VerbiRepo().FindByVerb(verbo):
        ilverbo = VerbiRepo().FindByVerb(verbo)
        verbiCondizionale = VerbiCondizionale().FindByVerb(verbo)
        return render_template('verbItaliano/italiano/italiano.html', ilverbo=ilverbo, verbiCondizionale=verbiCondizionale)
    else:
        ilverbo = RiflessiviRepo().FindByVerb(verbo)
        return render_template('verbItaliano/italiano/italiano.html', ilverbo=ilverbo)


@verbIta.route('/', methods=['GET', 'POST'])
def italianoAltroVerbo():

    verbo = str(request.form['verbo']).lower().strip()
    verbi = VerbiRepo().ListDistinctVerbs()
    if VerbiRepo().FindByVerb(verbo):
        ilverbo = VerbiRepo().FindByVerb(verbo)
        return render_template('verbItaliano/italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)
    else:
        try:
            ApiUltralingua(verbo)
            ilverbo = VerbiRepo().FindByVerb(verbo)
            return render_template('verbItaliano/italiano/italiano.html', verbi=verbi, ilverbo=ilverbo)
        except:
            flash(f'Verbo non trovato, trovane un altro', 'danger')
            return redirect(url_for('verbIta.italianoMain'))

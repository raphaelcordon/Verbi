from flask import render_template, session, redirect, url_for, Blueprint, request, flash, Flask, Response
from flask_recaptcha import ReCaptcha
from repository.verbItaliano.verbi_repos import VerbiRepository as VerbiRepo
from thirdparty.verbItaliano.gmail import UserEmail

verbInd = Blueprint('verbInd', __name__, url_prefix='')

reCaptchaConf = Flask(__name__)
reCaptchaConf.config['RECAPTCHA_SITE_KEY'] = '6LcdKBUeAAAAAPFhAJQrgi9uHRDIaV7mbNAYyxPq'
reCaptchaConf.config['RECAPTCHA_SECRET_KEY'] = '6LcdKBUeAAAAAGgOQDrijg1ru5dWjUPEvuYkiaZB'
recaptcha = ReCaptcha(reCaptchaConf)


@verbInd.route('/')
def index():

    CleanSession()
    verbi = VerbiRepo().ListDistinctVerbs()
    top20 = ('essere', 'avere', 'fare', 'dire', 'potere', 'volere', 'sapere', 'stare', 'dovere', 'vedere', 'andare',
             'venire', 'dare', 'parlare', 'trovare', 'sentire', 'lasciare', 'prendere', 'guardare', 'mettere')

    return render_template('verbItaliano/index.html', verbi=verbi, top20=top20)


@verbInd.route('/adm')
def adm():
    return render_template('verbItaliano/adm/adm.html')


@verbInd.route('/talkToUs', methods=['GET', 'POST'])
def talkToUs():
    if recaptcha.verify():  # to see if ReCaptcha is filled out
        UserEmail(
            request.form['name'],
            request.form['email'],
            request.form['subject'],
            request.form['message'])
        flash(f'Message successfully sent! :)', 'success')
        return redirect(request.referrer)
    else:
        flash(f'Fill up the reCaptcha before sending messages.', 'danger')
        return redirect(request.referrer)


@verbInd.route('/adm/verbiItaliano/', methods=['GET', 'POST'])
def admItaliano():
    get_verbo = str(request.form['verbo']).lower().strip()
    if VerbiRepo().FindByVerb(get_verbo):
        ilverbo = VerbiRepo().FindByVerb(get_verbo)
        return render_template('verbItaliano/adm/italiano.html', ilverbo=ilverbo)
    else:
        flash(f'Verbo non trovato, trovane un altro', 'danger')
        return redirect(url_for('ind.adm'))


@verbInd.route('/admItalianoUpdateVerbo', methods=['GET', 'POST'])
def admItalianoUpdateVerbo():

    updateVerbo()

    ilverbo = VerbiRepo().FindByVerb(str(request.form['infinitivoPresente']).lower().strip())
    flash(f'Verbo aggiornato con successo', 'success')
    return render_template('verbItaliano/adm/italiano.html', ilverbo=ilverbo)


@verbInd.route('/<ads>.<txt>')
def adsTxt(ads, txt):
    if ads == 'ads' and txt == 'txt':
        with open("ads.txt", "r") as f:
            content = f.read()
        return Response(content, mimetype='text/plain')
    else:
        return redirect(url_for('ind.index'))


def CleanSession():
    session['id'] = ''
    session['name'] = ''
    session['surname'] = ''
    session['password'] = ''
    session['email'] = ''


def updateVerbo():

    VerbiRepo().Edit(
        str(request.form['infinitivoPresente']).lower().strip(),
        str(request.form['infinitivoPassato']).lower().strip(),
        str(request.form['participioPresente']).lower().strip(),
        str(request.form['participioPassato']).lower().strip(),
        str(request.form['gerundioPresente']).lower().strip(),
        str(request.form['gerundioPassato']).lower().strip(),
        str(request.form['indicativoPresenteIo']).lower().strip(),
        str(request.form['indicativoPresenteTu']).lower().strip(),
        str(request.form['indicativoPresenteLui']).lower().strip(),
        str(request.form['indicativoPresenteNoi']).lower().strip(),
        str(request.form['indicativoPresenteVoi']).lower().strip(),
        str(request.form['indicativoPresenteLoro']).lower().strip(),
        str(request.form['indicativoPassatoProssimoIo']).lower().strip(),
        str(request.form['indicativoPassatoProssimoTu']).lower().strip(),
        str(request.form['indicativoPassatoProssimoLui']).lower().strip(),
        str(request.form['indicativoPassatoProssimoNoi']).lower().strip(),
        str(request.form['indicativoPassatoProssimoVoi']).lower().strip(),
        str(request.form['indicativoPassatoProssimoLoro']).lower().strip(),
        str(request.form['indicativoImperfettoIo']).lower().strip(),
        str(request.form['indicativoImperfettoTu']).lower().strip(),
        str(request.form['indicativoImperfettoLui']).lower().strip(),
        str(request.form['indicativoImperfettoNoi']).lower().strip(),
        str(request.form['indicativoImperfettoVoi']).lower().strip(),
        str(request.form['indicativoImperfettoLoro']).lower().strip(),
        str(request.form['indicativoTrapassatoProssimoIo']).lower().strip(),
        str(request.form['indicativoTrapassatoProssimoTu']).lower().strip(),
        str(request.form['indicativoTrapassatoProssimoLui']).lower().strip(),
        str(request.form['indicativoTrapassatoProssimoNoi']).lower().strip(),
        str(request.form['indicativoTrapassatoProssimoVoi']).lower().strip(),
        str(request.form['indicativoTrapassatoProssimoLoro']).lower().strip(),
        str(request.form['indicativoPassatoRemotoIo']).lower().strip(),
        str(request.form['indicativoPassatoRemotoTu']).lower().strip(),
        str(request.form['indicativoPassatoRemotoLui']).lower().strip(),
        str(request.form['indicativoPassatoRemotoNoi']).lower().strip(),
        str(request.form['indicativoPassatoRemotoVoi']).lower().strip(),
        str(request.form['indicativoPassatoRemotoLoro']).lower().strip(),
        str(request.form['indicativoTrapassatoRemotoIo']).lower().strip(),
        str(request.form['indicativoTrapassatoRemotoTu']).lower().strip(),
        str(request.form['indicativoTrapassatoRemotoLui']).lower().strip(),
        str(request.form['indicativoTrapassatoRemotoNoi']).lower().strip(),
        str(request.form['indicativoTrapassatoRemotoVoi']).lower().strip(),
        str(request.form['indicativoTrapassatoRemotoLoro']).lower().strip(),
        str(request.form['indicativoFuturoSempliceIo']).lower().strip(),
        str(request.form['indicativoFuturoSempliceTu']).lower().strip(),
        str(request.form['indicativoFuturoSempliceLui']).lower().strip(),
        str(request.form['indicativoFuturoSempliceNoi']).lower().strip(),
        str(request.form['indicativoFuturoSempliceVoi']).lower().strip(),
        str(request.form['indicativoFuturoSempliceLoro']).lower().strip(),
        str(request.form['indicativoFuturoAnterioreIo']).lower().strip(),
        str(request.form['indicativoFuturoAnterioreTu']).lower().strip(),
        str(request.form['indicativoFuturoAnterioreLui']).lower().strip(),
        str(request.form['indicativoFuturoAnterioreNoi']).lower().strip(),
        str(request.form['indicativoFuturoAnterioreVoi']).lower().strip(),
        str(request.form['indicativoFuturoAnterioreLoro']).lower().strip(),
        str(request.form['congiuntivoPresenteIo']).lower().strip(),
        str(request.form['congiuntivoPresenteTu']).lower().strip(),
        str(request.form['congiuntivoPresenteLui']).lower().strip(),
        str(request.form['congiuntivoPresenteNoi']).lower().strip(),
        str(request.form['congiuntivoPresenteVoi']).lower().strip(),
        str(request.form['congiuntivoPresenteLoro']).lower().strip(),
        str(request.form['congiuntivoPassatoIo']).lower().strip(),
        str(request.form['congiuntivoPassatoTu']).lower().strip(),
        str(request.form['congiuntivoPassatoLui']).lower().strip(),
        str(request.form['congiuntivoPassatoNoi']).lower().strip(),
        str(request.form['congiuntivoPassatoVoi']).lower().strip(),
        str(request.form['congiuntivoPassatoLoro']).lower().strip(),
        str(request.form['congiuntivoImperfettoIo']).lower().strip(),
        str(request.form['congiuntivoImperfettoTu']).lower().strip(),
        str(request.form['congiuntivoImperfettoLui']).lower().strip(),
        str(request.form['congiuntivoImperfettoNoi']).lower().strip(),
        str(request.form['congiuntivoImperfettoVoi']).lower().strip(),
        str(request.form['congiuntivoImperfettoLoro']).lower().strip(),
        str(request.form['congiuntivoTrapassatoIo']).lower().strip(),
        str(request.form['congiuntivoTrapassatoTu']).lower().strip(),
        str(request.form['congiuntivoTrapassatoLui']).lower().strip(),
        str(request.form['congiuntivoTrapassatoNoi']).lower().strip(),
        str(request.form['congiuntivoTrapassatoVoi']).lower().strip(),
        str(request.form['congiuntivoTrapassatoLoro']).lower().strip(),
        str(request.form['imperativoPresenteTu']).lower().strip(),
        str(request.form['imperativoPresenteLui']).lower().strip(),
        str(request.form['imperativoPresenteNoi']).lower().strip(),
        str(request.form['imperativoPresenteVoi']).lower().strip(),
        str(request.form['imperativoPresenteLoro']).lower().strip())

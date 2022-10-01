import requests
from repository.verbItaliano.verbi_repos import VerbiRepository as VerbiRepo

key = 'N78XT58I4LKRVFP3925Q'


class ApiUltralingua:
    def __init__(self, verbo):
        """
        Returns the five first artists accordingly the user's search
        :param name: User's search object
        """
        self.verbo = verbo
        self.indicativoPassatoProssimoIo = {'indicativoPassatoProssimoIo': ''}
        self.listVerbs = {}
        self.bringVerb()
        self.registryNewVerb()

    def bringVerb(self):
        api_url = "https://api.ultralingua.com/api/2.0//conjugations/it/" + self.verbo + "?key=" + key
        response = requests.get(api_url)
        response = response.json()
        for item in response[0]['conjugations']:
            # Main Verbs definition
            self.mainVerbs(item)

            # Indicativo | PRESENTE
            self.indicativoPresente(item)

            # Indicativo | PASSATO PROSSIMO
            self.indicativoPassatoProssimo(item)

            # Indicativo | IMPERFETTO
            self.indicativoImperfetto(item)

            # Indicativo | TRAPASSATO PROSSIMO
            self.indicativoTrapassatoProssimo(item)

            # Indicativo | PASSATO REMOTO
            self.indicativoPassatoRemoto(item)

            # Indicativo | TRAPASSATO REMOTO
            self.indicativoTrapassatoRemoto(item)

            # Indicativo | FUTURO SEMPLICE
            self.indicativoFuturoSemplice(item)

            # Indicativo | FUTURO ANTERIORE
            self.indicativoFuturoAnteriore(item)

            # Congiuntivo | PRESENTE
            self.congiuntivoPresente(item)

            # Congiuntivo | PASSATO
            self.congiuntivoPassato(item)

            # Congiuntivo | IMPERFETTO
            self.congiuntivoImperfetto(item)

            # Congiuntivo | TRAPASSATO
            self.congiuntivoTrapassato(item)

            # Imperativo
            self.imperativo(item)

        return self.listVerbs

    def mainVerbs(self, item):
        if item['partofspeech']['tense'] == 'infinitive':
            verbo = {'infinitivoPresente': item['surfaceform']}
            self.listVerbs.update(verbo)

        if item['partofspeech']['tense'] == 'presentparticiple':
            verbo = {'participioPresente': item['surfaceform']}
            self.listVerbs.update(verbo)

        if item['partofspeech']['tense'] == 'gerund':
            verbo = {'gerundioPresente': item['surfaceform']}
            self.listVerbs.update(verbo)

    #  ---   I N D I C A T I V O   ---
    def indicativoPresente(self, item):

        # PRESENTE IO
        if item['partofspeech']['tense'] == 'present' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPresenteIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE TU
        if item['partofspeech']['tense'] == 'present' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPresenteTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE LUI
        if item['partofspeech']['tense'] == 'present' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPresenteLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE NOI
        if item['partofspeech']['tense'] == 'present' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPresenteNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE VOI
        if item['partofspeech']['tense'] == 'present' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPresenteVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE LORO
        if item['partofspeech']['tense'] == 'present' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPresenteLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoPassatoProssimo(self, item):

        # PASSATO PROSSIMO IO
        verbo = {'indicativoPassatoProssimoIo': ''}
        try:
            if item['partofspeech']['tense'] == 'presentperfect' and item['partofspeech']['person'] == 'first' and \
                    item['partofspeech']['number'] == 'singular':
                verbo = {'indicativoPassatoProssimoIo': item['surfaceform']}
        except:

            verbo = {'indicativoPassatoProssimoIo': ''}
        finally:
            self.listVerbs.update(verbo)


        # PASSATO PROSSIMO TU
        if item['partofspeech']['tense'] == 'presentperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPassatoProssimoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO PROSSIMO LUI
        if item['partofspeech']['tense'] == 'presentperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPassatoProssimoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO PROSSIMO NOI
        if item['partofspeech']['tense'] == 'presentperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPassatoProssimoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO PROSSIMO VOI
        if item['partofspeech']['tense'] == 'presentperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPassatoProssimoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO PROSSIMO LORO
        if item['partofspeech']['tense'] == 'presentperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPassatoProssimoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoImperfetto(self, item):

        # IMPERFETTO IO
        if item['partofspeech']['tense'] == 'imperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoImperfettoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO TU
        if item['partofspeech']['tense'] == 'imperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoImperfettoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO LUI
        if item['partofspeech']['tense'] == 'imperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoImperfettoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO NOI
        if item['partofspeech']['tense'] == 'imperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoImperfettoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO VOI
        if item['partofspeech']['tense'] == 'imperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoImperfettoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO LORO
        if item['partofspeech']['tense'] == 'imperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoImperfettoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoTrapassatoProssimo(self, item):

        # TRAPASSATO PROSSIMO IO
        if item['partofspeech']['tense'] == 'pastperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoTrapassatoProssimoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO PROSSIMO TU
        if item['partofspeech']['tense'] == 'pastperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoTrapassatoProssimoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO PROSSIMO LUI
        if item['partofspeech']['tense'] == 'pastperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoTrapassatoProssimoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO PROSSIMO NOI
        if item['partofspeech']['tense'] == 'pastperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoTrapassatoProssimoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO PROSSIMO VOI
        if item['partofspeech']['tense'] == 'pastperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoTrapassatoProssimoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO PROSSIMO LORO
        if item['partofspeech']['tense'] == 'pastperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoTrapassatoProssimoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoPassatoRemoto(self, item):

        # PASSATO REMOTO IO
        if item['partofspeech']['tense'] == 'past' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPassatoRemotoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO REMOTO TU
        if item['partofspeech']['tense'] == 'past' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPassatoRemotoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO REMOTO LUI
        if item['partofspeech']['tense'] == 'past' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoPassatoRemotoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO REMOTO NOI
        if item['partofspeech']['tense'] == 'past' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPassatoRemotoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO REMOTO VOI
        if item['partofspeech']['tense'] == 'past' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPassatoRemotoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO REMOTO LORO
        if item['partofspeech']['tense'] == 'past' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoPassatoRemotoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoTrapassatoRemoto(self, item):

        # TRAPASSATO REMOTO IO
        if item['partofspeech']['tense'] == 'pastanterior' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoTrapassatoRemotoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO REMOTO TU
        if item['partofspeech']['tense'] == 'pastanterior' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoTrapassatoRemotoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO REMOTO LUI
        if item['partofspeech']['tense'] == 'pastanterior' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoTrapassatoRemotoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO REMOTO NOI
        if item['partofspeech']['tense'] == 'pastanterior' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoTrapassatoRemotoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO REMOTO VOI
        if item['partofspeech']['tense'] == 'pastanterior' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoTrapassatoRemotoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO REMOTO LORO
        if item['partofspeech']['tense'] == 'pastanterior' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoTrapassatoRemotoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoFuturoSemplice(self, item):

        # FUTURO SEMPLICE IO
        if item['partofspeech']['tense'] == 'future' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoFuturoSempliceIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE TU
        if item['partofspeech']['tense'] == 'future' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoFuturoSempliceTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE LUI
        if item['partofspeech']['tense'] == 'future' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoFuturoSempliceLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE NOI
        if item['partofspeech']['tense'] == 'future' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoFuturoSempliceNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE VOI
        if item['partofspeech']['tense'] == 'future' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoFuturoSempliceVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE LORO
        if item['partofspeech']['tense'] == 'future' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoFuturoSempliceLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def indicativoFuturoAnteriore(self, item):

        # FUTURO SEMPLICE IO
        if item['partofspeech']['tense'] == 'futureperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoFuturoAnterioreIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE TU
        if item['partofspeech']['tense'] == 'futureperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoFuturoAnterioreTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE LUI
        if item['partofspeech']['tense'] == 'futureperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'indicativoFuturoAnterioreLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE NOI
        if item['partofspeech']['tense'] == 'futureperfect' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoFuturoAnterioreNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE VOI
        if item['partofspeech']['tense'] == 'futureperfect' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoFuturoAnterioreVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # FUTURO SEMPLICE LORO
        if item['partofspeech']['tense'] == 'futureperfect' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'indicativoFuturoAnterioreLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    #  ---   C O N G I U N T I V O   ---
    def congiuntivoPresente(self, item):

        # PRESENTE IO
        if item['partofspeech']['tense'] == 'presentsubjunctive' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoPresenteIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE TU
        if item['partofspeech']['tense'] == 'presentsubjunctive' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoPresenteTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE LUI
        if item['partofspeech']['tense'] == 'presentsubjunctive' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoPresenteLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE NOI
        if item['partofspeech']['tense'] == 'presentsubjunctive' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoPresenteNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE VOI
        if item['partofspeech']['tense'] == 'presentsubjunctive' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoPresenteVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE LORO
        if item['partofspeech']['tense'] == 'presentsubjunctive' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoPresenteLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def congiuntivoPassato(self, item):

        # PASSATO IO
        if item['partofspeech']['tense'] == 'presentperfectsubjunctive' and item['partofspeech'][
            'person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoPassatoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO TU
        if item['partofspeech']['tense'] == 'presentperfectsubjunctive' and item['partofspeech'][
            'person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoPassatoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO LUI
        if item['partofspeech']['tense'] == 'presentperfectsubjunctive' and item['partofspeech'][
            'person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoPassatoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO NOI
        if item['partofspeech']['tense'] == 'presentperfectsubjunctive' and item['partofspeech'][
            'person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoPassatoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO VOI
        if item['partofspeech']['tense'] == 'presentperfectsubjunctive' and item['partofspeech'][
            'person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoPassatoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PASSATO LORO
        if item['partofspeech']['tense'] == 'presentperfectsubjunctive' and item['partofspeech'][
            'person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoPassatoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def congiuntivoImperfetto(self, item):

        # IMPERFETTO IO
        if item['partofspeech']['tense'] == 'imperfectsubjunctive' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoImperfettoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO TU
        if item['partofspeech']['tense'] == 'imperfectsubjunctive' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoImperfettoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO LUI
        if item['partofspeech']['tense'] == 'imperfectsubjunctive' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoImperfettoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO NOI
        if item['partofspeech']['tense'] == 'imperfectsubjunctive' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoImperfettoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO VOI
        if item['partofspeech']['tense'] == 'imperfectsubjunctive' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoImperfettoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # IMPERFETTO LORO
        if item['partofspeech']['tense'] == 'imperfectsubjunctive' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoImperfettoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    def congiuntivoTrapassato(self, item):

        # TRAPASSATO IO
        if item['partofspeech']['tense'] == 'pastperfectsubjunctive' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoTrapassatoIo': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO TU
        if item['partofspeech']['tense'] == 'pastperfectsubjunctive' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoTrapassatoTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO LUI
        if item['partofspeech']['tense'] == 'pastperfectsubjunctive' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'congiuntivoTrapassatoLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO NOI
        if item['partofspeech']['tense'] == 'pastperfectsubjunctive' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoTrapassatoNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO VOI
        if item['partofspeech']['tense'] == 'pastperfectsubjunctive' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoTrapassatoVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # TRAPASSATO LORO
        if item['partofspeech']['tense'] == 'pastperfectsubjunctive' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'congiuntivoTrapassatoLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    #  ---   I M P E R A T I V O   ---
    def imperativo(self, item):

        # PRESENTE TU
        if item['partofspeech']['tense'] == 'imperative' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'imperativoPresenteTu': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE LUI
        if item['partofspeech']['tense'] == 'imperative' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'singular':
            verbo = {'imperativoPresenteLui': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE NOI
        if item['partofspeech']['tense'] == 'imperative' and item['partofspeech']['person'] == 'first' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'imperativoPresenteNoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE VOI
        if item['partofspeech']['tense'] == 'imperative' and item['partofspeech']['person'] == 'second' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'imperativoPresenteVoi': item['surfaceform']}
            self.listVerbs.update(verbo)

        # PRESENTE LORO
        if item['partofspeech']['tense'] == 'imperative' and item['partofspeech']['person'] == 'third' and \
                item['partofspeech']['number'] == 'plural':
            verbo = {'imperativoPresenteLoro': item['surfaceform']}
            self.listVerbs.update(verbo)

    #  ---   REGISTERING NEW VERB IN DB   ---
    def registryNewVerb(self):
        VerbiRepo().New(
            self.listVerbs['infinitivoPresente'], self.listVerbs['participioPresente'],
            self.listVerbs['gerundioPresente'], self.listVerbs['indicativoPresenteIo'],
            self.listVerbs['indicativoPresenteTu'],
            self.listVerbs['indicativoPresenteLui'], self.listVerbs['indicativoPresenteNoi'],
            self.listVerbs['indicativoPresenteVoi'], self.listVerbs['indicativoPresenteLoro'],
            self.listVerbs['indicativoPassatoProssimoIo'], self.listVerbs['indicativoPassatoProssimoTu'],
            self.listVerbs['indicativoPassatoProssimoLui'],
            self.listVerbs['indicativoPassatoProssimoNoi'], self.listVerbs['indicativoPassatoProssimoVoi'],
            self.listVerbs['indicativoPassatoProssimoLoro'],
            self.listVerbs['indicativoImperfettoIo'], self.listVerbs['indicativoImperfettoTu'],
            self.listVerbs['indicativoImperfettoLui'], self.listVerbs['indicativoImperfettoNoi'],
            self.listVerbs['indicativoImperfettoVoi'], self.listVerbs['indicativoImperfettoLoro'],
            self.listVerbs['indicativoTrapassatoProssimoIo'],
            self.listVerbs['indicativoTrapassatoProssimoTu'], self.listVerbs['indicativoTrapassatoProssimoLui'],
            self.listVerbs['indicativoTrapassatoProssimoNoi'],
            self.listVerbs['indicativoTrapassatoProssimoVoi'], self.listVerbs['indicativoTrapassatoProssimoLoro'],
            self.listVerbs['indicativoPassatoRemotoIo'],
            self.listVerbs['indicativoPassatoRemotoTu'], self.listVerbs['indicativoPassatoRemotoLui'],
            self.listVerbs['indicativoPassatoRemotoNoi'],
            self.listVerbs['indicativoPassatoRemotoVoi'], self.listVerbs['indicativoPassatoRemotoLoro'],
            self.listVerbs['indicativoTrapassatoRemotoIo'],
            self.listVerbs['indicativoTrapassatoRemotoTu'], self.listVerbs['indicativoTrapassatoRemotoLui'],
            self.listVerbs['indicativoTrapassatoRemotoNoi'],
            self.listVerbs['indicativoTrapassatoRemotoVoi'], self.listVerbs['indicativoTrapassatoRemotoLoro'],
            self.listVerbs['indicativoFuturoSempliceIo'],
            self.listVerbs['indicativoFuturoSempliceTu'], self.listVerbs['indicativoFuturoSempliceLui'],
            self.listVerbs['indicativoFuturoSempliceNoi'],
            self.listVerbs['indicativoFuturoSempliceVoi'], self.listVerbs['indicativoFuturoSempliceLoro'],
            self.listVerbs['indicativoFuturoAnterioreIo'],
            self.listVerbs['indicativoFuturoAnterioreTu'], self.listVerbs['indicativoFuturoAnterioreLui'],
            self.listVerbs['indicativoFuturoAnterioreNoi'],
            self.listVerbs['indicativoFuturoAnterioreVoi'], self.listVerbs['indicativoFuturoAnterioreLoro'],
            self.listVerbs['congiuntivoPresenteIo'],
            self.listVerbs['congiuntivoPresenteTu'], self.listVerbs['congiuntivoPresenteLui'],
            self.listVerbs['congiuntivoPresenteNoi'], self.listVerbs['congiuntivoPresenteVoi'],
            self.listVerbs['congiuntivoPresenteLoro'], self.listVerbs['congiuntivoPassatoIo'],
            self.listVerbs['congiuntivoPassatoTu'], self.listVerbs['congiuntivoPassatoLui'],
            self.listVerbs['congiuntivoPassatoNoi'], self.listVerbs['congiuntivoPassatoVoi'],
            self.listVerbs['congiuntivoPassatoLoro'], self.listVerbs['congiuntivoImperfettoIo'],
            self.listVerbs['congiuntivoImperfettoTu'], self.listVerbs['congiuntivoImperfettoLui'],
            self.listVerbs['congiuntivoImperfettoNoi'], self.listVerbs['congiuntivoImperfettoVoi'],
            self.listVerbs['congiuntivoImperfettoLoro'], self.listVerbs['congiuntivoTrapassatoIo'],
            self.listVerbs['congiuntivoTrapassatoTu'], self.listVerbs['congiuntivoTrapassatoLui'],
            self.listVerbs['congiuntivoTrapassatoNoi'], self.listVerbs['congiuntivoTrapassatoVoi'],
            self.listVerbs['congiuntivoTrapassatoLoro'], self.listVerbs['imperativoPresenteTu'],
            self.listVerbs['imperativoPresenteLui'], self.listVerbs['imperativoPresenteNoi'],
            self.listVerbs['imperativoPresenteVoi'], self.listVerbs['imperativoPresenteLoro'])

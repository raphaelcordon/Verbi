from .base_repos import PostgreDB
from models.italiano_model import Italiano, ItalianoOneVerb, Verbi


class VerbiRepository:

    # <- Register a new 'Verb' in the table ->
    def New(self, infinitivoPresente='', participioPresente='', gerundioPresente='', indicativoPresenteIo='',
            indicativoPresenteTu='', indicativoPresenteLui='', indicativoPresenteNoi='', indicativoPresenteVoi='',
            indicativoPresenteLoro='', indicativoPassatoProssimoIo='', indicativoPassatoProssimoTu='',
            indicativoPassatoProssimoLui='', indicativoPassatoProssimoNoi='', indicativoPassatoProssimoVoi='',
            indicativoPassatoProssimoLoro='', indicativoImperfettoIo='', indicativoImperfettoTu='',
            indicativoImperfettoLui='', indicativoImperfettoNoi='', indicativoImperfettoVoi='',
            indicativoImperfettoLoro='', indicativoTrapassatoProssimoIo='', indicativoTrapassatoProssimoTu='',
            indicativoTrapassatoProssimoLui='', indicativoTrapassatoProssimoNoi='', indicativoTrapassatoProssimoVoi='',
            indicativoTrapassatoProssimoLoro='', indicativoPassatoRemotoIo='', indicativoPassatoRemotoTu='',
            indicativoPassatoRemotoLui='', indicativoPassatoRemotoNoi='', indicativoPassatoRemotoVoi='',
            indicativoPassatoRemotoLoro='', indicativoTrapassatoRemotoIo='', indicativoTrapassatoRemotoTu='',
            indicativoTrapassatoRemotoLui='', indicativoTrapassatoRemotoNoi='', indicativoTrapassatoRemotoVoi='',
            indicativoTrapassatoRemotoLoro='', indicativoFuturoSempliceIo='', indicativoFuturoSempliceTu='',
            indicativoFuturoSempliceLui='', indicativoFuturoSempliceNoi='', indicativoFuturoSempliceVoi='',
            indicativoFuturoSempliceLoro='', indicativoFuturoAnterioreIo='', indicativoFuturoAnterioreTu='',
            indicativoFuturoAnterioreLui='', indicativoFuturoAnterioreNoi='', indicativoFuturoAnterioreVoi='',
            indicativoFuturoAnterioreLoro='', congiuntivoPresenteIo='', congiuntivoPresenteTu='',
            congiuntivoPresenteLui='', congiuntivoPresenteNoi='', congiuntivoPresenteVoi='', congiuntivoPresenteLoro='',
            congiuntivoPassatoIo='', congiuntivoPassatoTu='', congiuntivoPassatoLui='', congiuntivoPassatoNoi='',
            congiuntivoPassatoVoi='', congiuntivoPassatoLoro='', congiuntivoImperfettoIo='', congiuntivoImperfettoTu='',
            congiuntivoImperfettoLui='', congiuntivoImperfettoNoi='', congiuntivoImperfettoVoi='',
            congiuntivoImperfettoLoro='',congiuntivoTrapassatoIo='', congiuntivoTrapassatoTu='',
            congiuntivoTrapassatoLui='', congiuntivoTrapassatoNoi='', congiuntivoTrapassatoVoi='',
            congiuntivoTrapassatoLoro='', imperativoPresenteTu='', imperativoPresenteLui='',
            imperativoPresenteNoi='', imperativoPresenteVoi='', imperativoPresenteLoro=''):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.verbi (infinitivoPresente, infinitivoPassato, participioPresente, participioPassato, " \
                     f"gerundioPresente, gerundioPassato, indicativoPresenteIo, indicativoPresenteTu, indicativoPresenteLui," \
                     f"indicativoPresenteNoi, indicativoPresenteVoi, indicativoPresenteLoro, indicativoPassatoProssimoIo," \
                     f"indicativoPassatoProssimoTu, indicativoPassatoProssimoLui, indicativoPassatoProssimoNoi," \
                     f"indicativoPassatoProssimoVoi, indicativoPassatoProssimoLoro, indicativoImperfettoIo," \
                     f"indicativoImperfettoTu, indicativoImperfettoLui, indicativoImperfettoNoi, indicativoImperfettoVoi," \
                     f"indicativoImperfettoLoro, indicativoTrapassatoProssimoIo, indicativoTrapassatoProssimoTu," \
                     f"indicativoTrapassatoProssimoLui, indicativoTrapassatoProssimoNoi, indicativoTrapassatoProssimoVoi," \
                     f"indicativoTrapassatoProssimoLoro, indicativoPassatoRemotoIo, indicativoPassatoRemotoTu," \
                     f"indicativoPassatoRemotoLui, indicativoPassatoRemotoNoi, indicativoPassatoRemotoVoi," \
                     f"indicativoPassatoRemotoLoro, indicativoTrapassatoRemotoIo, indicativoTrapassatoRemotoTu," \
                     f"indicativoTrapassatoRemotoLui, indicativoTrapassatoRemotoNoi, indicativoTrapassatoRemotoVoi," \
                     f"indicativoTrapassatoRemotoLoro, indicativoFuturoSempliceIo, indicativoFuturoSempliceTu," \
                     f"indicativoFuturoSempliceLui, indicativoFuturoSempliceNoi, indicativoFuturoSempliceVoi," \
                     f"indicativoFuturoSempliceLoro, indicativoFuturoAnterioreIo, indicativoFuturoAnterioreTu," \
                     f"indicativoFuturoAnterioreLui, indicativoFuturoAnterioreNoi, indicativoFuturoAnterioreVoi," \
                     f"indicativoFuturoAnterioreLoro, congiuntivoPresenteIo, congiuntivoPresenteTu, congiuntivoPresenteLui," \
                     f"congiuntivoPresenteNoi, congiuntivoPresenteVoi, congiuntivoPresenteLoro, congiuntivoPassatoIo," \
                     f"congiuntivoPassatoTu, congiuntivoPassatoLui, congiuntivoPassatoNoi, congiuntivoPassatoVoi," \
                     f"congiuntivoPassatoLoro, congiuntivoImperfettoIo, congiuntivoImperfettoTu, congiuntivoImperfettoLui," \
                     f"congiuntivoImperfettoNoi, congiuntivoImperfettoVoi, congiuntivoImperfettoLoro, congiuntivoTrapassatoIo," \
                     f"congiuntivoTrapassatoTu, congiuntivoTrapassatoLui, congiuntivoTrapassatoNoi, congiuntivoTrapassatoVoi," \
                     f"congiuntivoTrapassatoLoro, imperativoPresenteTu, imperativoPresenteLui, imperativoPresenteNoi," \
                     f"imperativoPresenteVoi, imperativoPresenteLoro) " \
                     f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     f"%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     f"%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     f"%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s)"
            db.queryParams(insert, (
                infinitivoPresente, '', participioPresente, '', gerundioPresente, '', indicativoPresenteIo,
                indicativoPresenteTu,
                indicativoPresenteLui, indicativoPresenteNoi, indicativoPresenteVoi, indicativoPresenteLoro,
                indicativoPassatoProssimoIo, indicativoPassatoProssimoTu, indicativoPassatoProssimoLui,
                indicativoPassatoProssimoNoi, indicativoPassatoProssimoVoi, indicativoPassatoProssimoLoro,
                indicativoImperfettoIo, indicativoImperfettoTu, indicativoImperfettoLui, indicativoImperfettoNoi,
                indicativoImperfettoVoi, indicativoImperfettoLoro, indicativoTrapassatoProssimoIo,
                indicativoTrapassatoProssimoTu, indicativoTrapassatoProssimoLui, indicativoTrapassatoProssimoNoi,
                indicativoTrapassatoProssimoVoi, indicativoTrapassatoProssimoLoro, indicativoPassatoRemotoIo,
                indicativoPassatoRemotoTu, indicativoPassatoRemotoLui, indicativoPassatoRemotoNoi,
                indicativoPassatoRemotoVoi, indicativoPassatoRemotoLoro, indicativoTrapassatoRemotoIo,
                indicativoTrapassatoRemotoTu, indicativoTrapassatoRemotoLui, indicativoTrapassatoRemotoNoi,
                indicativoTrapassatoRemotoVoi, indicativoTrapassatoRemotoLoro, indicativoFuturoSempliceIo,
                indicativoFuturoSempliceTu, indicativoFuturoSempliceLui, indicativoFuturoSempliceNoi,
                indicativoFuturoSempliceVoi, indicativoFuturoSempliceLoro, indicativoFuturoAnterioreIo,
                indicativoFuturoAnterioreTu, indicativoFuturoAnterioreLui, indicativoFuturoAnterioreNoi,
                indicativoFuturoAnterioreVoi, indicativoFuturoAnterioreLoro, congiuntivoPresenteIo,
                congiuntivoPresenteTu, congiuntivoPresenteLui, congiuntivoPresenteNoi, congiuntivoPresenteVoi,
                congiuntivoPresenteLoro, congiuntivoPassatoIo, congiuntivoPassatoTu, congiuntivoPassatoLui,
                congiuntivoPassatoNoi, congiuntivoPassatoVoi, congiuntivoPassatoLoro, congiuntivoImperfettoIo,
                congiuntivoImperfettoTu, congiuntivoImperfettoLui, congiuntivoImperfettoNoi, congiuntivoImperfettoVoi,
                congiuntivoImperfettoLoro, congiuntivoTrapassatoIo, congiuntivoTrapassatoTu, congiuntivoTrapassatoLui,
                congiuntivoTrapassatoNoi, congiuntivoTrapassatoVoi, congiuntivoTrapassatoLoro, imperativoPresenteTu,
                imperativoPresenteLui, imperativoPresenteNoi, imperativoPresenteVoi, imperativoPresenteLoro
            ))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List Verbs registered ->
    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.verbi")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Verb finder to redirect to the execution page ->
    def FindByVerb(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.verbi where infinitivoPresente = '{verbo}'")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List only the column "Verbo" ->
    def ListDistinctVerbs(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT DISTINCT infinitivoPresente FROM public.verbi")
            return self.__toListDistinctVerbs(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete an user on DB ->
    def Delete(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.verbi WHERE infinitivoPresente = {verbo}")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toList(self, item):
        def add(item):
            try:
                return self.__toOne(item)
            except Exception as exp:
                print(exp)

        try:
            return list(map(add, item))
        except Exception as exp:
            print(exp)

    def __toOne(self, item):
        try:
            return Verbi(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9],
                         item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18],
                         item[19],
                         item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28],
                         item[29],
                         item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38],
                         item[39],
                         item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48],
                         item[49],
                         item[50], item[51], item[52], item[53], item[54], item[55], item[56], item[57], item[58],
                         item[59],
                         item[60], item[61], item[62], item[63], item[64], item[65], item[66], item[67], item[68],
                         item[69],
                         item[70], item[71], item[72], item[73], item[74], item[75], item[76], item[77], item[78],
                         item[79],
                         item[80], item[81], item[82], item[83]
                         )
        except Exception as exp:
            print(exp)

    def __toListDistinctVerbs(self, item):
        def add(item):
            try:
                return self.__toOneVerb(item)
            except Exception as exp:
                print(exp)

        try:
            return list(map(add, item))
        except Exception as exp:
            print(exp)

    def __toOneVerb(self, item):
        try:
            return ItalianoOneVerb(item[0])
        except Exception as exp:
            print(exp)

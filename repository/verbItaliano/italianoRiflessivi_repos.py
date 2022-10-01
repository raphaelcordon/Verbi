from .base_repos import PostgreDB
from models.verbItaliano.italianoRiflessivi_model import ItalianoOneVerb, Verbi


class VerbiRepository:

    # <- Register a new 'Verb' in the table ->
    def New(self, riflessivo='', infinitivoPresente='', infinitivoPassato='', participioPresente='',
            participioPassato='', gerundioPresente='', gerundioPassato='', indicativoPresenteIo='',
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
            indicativoFuturoAnterioreLoro='',
            condizionalePresenteIo='', condizionalePresenteTu='',
            condizionalePresenteLui='', condizionalePresenteNoi='', condizionalePresenteVoi='',
            condizionalePresenteLoro='', condizionalePassatoIo='', condizionalePassatoTu='',
            condizionalePassatoLui='', condizionalePassatoNoi='', condizionalePassatoVoi='',
            condizionalePassatoLoro='',
            congiuntivoPresenteIo='', congiuntivoPresenteTu='',
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
            insert = f"INSERT INTO public.italianriflessivi (riflessivo, infinitivoPresente, infinitivoPassato, participioPresente, participioPassato, " \
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
                     f"indicativoFuturoAnterioreLoro, condizionalePresenteIo, condizionalePresenteTu, " \
                     f"condizionalePresenteLui, condizionalePresenteNoi, condizionalePresenteVoi," \
                     f"condizionalePresenteLoro, condizionalePassatoIo, condizionalePassatoTu," \
                     f"condizionalePassatoLui, condizionalePassatoNoi, condizionalePassatoVoi, condizionalePassatoLoro," \
                     f"congiuntivoPresenteIo, congiuntivoPresenteTu, congiuntivoPresenteLui," \
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
                     f"%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     f"%s, %s,  %s, %s, %s, %s, %s, %s, %s)"
            db.queryParams(insert, (
                riflessivo, infinitivoPresente, infinitivoPassato, participioPresente, participioPassato,
                gerundioPresente, gerundioPassato, indicativoPresenteIo,
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
                indicativoFuturoAnterioreVoi, indicativoFuturoAnterioreLoro,
                condizionalePresenteIo, condizionalePresenteTu, condizionalePresenteLui,
                condizionalePresenteNoi, condizionalePresenteVoi, condizionalePresenteLoro, condizionalePassatoIo,
                condizionalePassatoTu, condizionalePassatoLui, condizionalePassatoNoi, condizionalePassatoVoi,
                condizionalePassatoLoro, congiuntivoPresenteIo,
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
            db.query(f"SELECT * FROM public.italianriflessivi")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Verb finder to redirect to the execution page ->
    def FindByVerb(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.italianriflessivi where infinitivoPresente = '{verbo}'")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List only the column "Verbo" ->
    def ListDistinctVerbs(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT DISTINCT infinitivoPresente FROM public.italianriflessivi")
            return self.__toListDistinctVerbs(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def Edit(self, riflessivo='', infinitivoPresente='', infinitivoPassato='', participioPresente='',
            participioPassato='', gerundioPresente='', gerundioPassato='', indicativoPresenteIo='',
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
            indicativoFuturoAnterioreLoro='',
            condizionalePresenteIo='', condizionalePresenteTu='',
            condizionalePresenteLui='', condizionalePresenteNoi='', condizionalePresenteVoi='',
            condizionalePresenteLoro='', condizionalePassatoIo='', condizionalePassatoTu='',
            condizionalePassatoLui='', condizionalePassatoNoi='', condizionalePassatoVoi='',
            condizionalePassatoLoro='',
            congiuntivoPresenteIo='', congiuntivoPresenteTu='',
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
            updating_query = f"update public.italianriflessivi set riflessivo=%s, infinitivoPresente=%s, infinitivoPassato=%s, participioPresente=%s, participioPassato=%s, " \
                             f"gerundioPresente=%s, gerundioPassato=%s, indicativoPresenteIo=%s, indicativoPresenteTu=%s, indicativoPresenteLui=%s," \
                             f"indicativoPresenteNoi=%s, indicativoPresenteVoi=%s, indicativoPresenteLoro=%s, indicativoPassatoProssimoIo=%s," \
                             f"indicativoPassatoProssimoTu=%s, indicativoPassatoProssimoLui=%s, indicativoPassatoProssimoNoi=%s," \
                             f"indicativoPassatoProssimoVoi=%s, indicativoPassatoProssimoLoro=%s, indicativoImperfettoIo=%s," \
                             f"indicativoImperfettoTu=%s, indicativoImperfettoLui=%s, indicativoImperfettoNoi=%s, indicativoImperfettoVoi=%s," \
                             f"indicativoImperfettoLoro=%s, indicativoTrapassatoProssimoIo=%s, indicativoTrapassatoProssimoTu=%s," \
                             f"indicativoTrapassatoProssimoLui=%s, indicativoTrapassatoProssimoNoi=%s, indicativoTrapassatoProssimoVoi=%s," \
                             f"indicativoTrapassatoProssimoLoro=%s, indicativoPassatoRemotoIo=%s, indicativoPassatoRemotoTu=%s," \
                             f"indicativoPassatoRemotoLui=%s, indicativoPassatoRemotoNoi=%s, indicativoPassatoRemotoVoi=%s," \
                             f"indicativoPassatoRemotoLoro=%s, indicativoTrapassatoRemotoIo=%s, indicativoTrapassatoRemotoTu=%s," \
                             f"indicativoTrapassatoRemotoLui=%s, indicativoTrapassatoRemotoNoi=%s, indicativoTrapassatoRemotoVoi=%s," \
                             f"indicativoTrapassatoRemotoLoro=%s, indicativoFuturoSempliceIo=%s, indicativoFuturoSempliceTu=%s," \
                             f"indicativoFuturoSempliceLui=%s, indicativoFuturoSempliceNoi=%s, indicativoFuturoSempliceVoi=%s," \
                             f"indicativoFuturoSempliceLoro=%s, indicativoFuturoAnterioreIo=%s, indicativoFuturoAnterioreTu=%s," \
                             f"indicativoFuturoAnterioreLui=%s, indicativoFuturoAnterioreNoi=%s, indicativoFuturoAnterioreVoi=%s," \
                             f"indicativoFuturoAnterioreLoro=%s, condizionalePresenteIo=%s, condizionalePresenteTu=%s, condizionalePresenteLui=%s," \
                             f"condizionalePresenteNoi=%s, condizionalePresenteVoi=%s, condizionalePresenteLoro=%s, condizionalePassatoIo=%s," \
                             f"condizionalePassatoTu=%s, condizionalePassatoLui=%s, condizionalePassatoNoi=%s," \
                             f"condizionalePassatoVoi=%s, condizionalePassatoLoro=%s, congiuntivoPresenteIo=%s, " \
                             f"congiuntivoPresenteTu=%s, congiuntivoPresenteLui=%s," \
                             f"congiuntivoPresenteNoi=%s, congiuntivoPresenteVoi=%s, congiuntivoPresenteLoro=%s, congiuntivoPassatoIo=%s," \
                             f"congiuntivoPassatoTu=%s, congiuntivoPassatoLui=%s, congiuntivoPassatoNoi=%s, congiuntivoPassatoVoi=%s," \
                             f"congiuntivoPassatoLoro=%s, congiuntivoImperfettoIo=%s, congiuntivoImperfettoTu=%s, congiuntivoImperfettoLui=%s," \
                             f"congiuntivoImperfettoNoi=%s, congiuntivoImperfettoVoi=%s, congiuntivoImperfettoLoro=%s, congiuntivoTrapassatoIo=%s," \
                             f"congiuntivoTrapassatoTu=%s, congiuntivoTrapassatoLui=%s, congiuntivoTrapassatoNoi=%s, congiuntivoTrapassatoVoi=%s," \
                             f"congiuntivoTrapassatoLoro=%s, imperativoPresenteTu=%s, imperativoPresenteLui=%s, imperativoPresenteNoi=%s," \
                             f"imperativoPresenteVoi=%s, imperativoPresenteLoro=%s where infinitivoPresente='{infinitivoPresente}'"
            db.queryParams(updating_query, (riflessivo,
            infinitivoPresente, infinitivoPassato, participioPresente, participioPassato, gerundioPresente,
            gerundioPassato, indicativoPresenteIo,
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
            indicativoFuturoAnterioreVoi, indicativoFuturoAnterioreLoro, condizionalePresenteIo, condizionalePresenteTu,
            condizionalePresenteLui, condizionalePresenteNoi, condizionalePresenteVoi, condizionalePresenteLoro,
            condizionalePassatoIo, condizionalePassatoTu, condizionalePassatoLui, condizionalePassatoNoi,
            condizionalePassatoVoi, condizionalePassatoLoro, congiuntivoPresenteIo,
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

    # <- Delete an user on DB ->
    def Delete(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.italianriflessivi WHERE infinitivoPresente = {verbo}")
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
                         item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27],
                         item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36],
                         item[37], item[38],  item[39], item[40], item[41], item[42], item[43], item[44], item[45],
                         item[46], item[47], item[48], item[49], item[50], item[51], item[52], item[53], item[54],
                         item[55], item[56], item[57], item[58], item[59], item[60], item[61], item[62], item[63],
                         item[64], item[65], item[66], item[67], item[68], item[69], item[70], item[71], item[72],
                         item[73], item[74], item[75], item[76], item[77], item[78], item[79], item[80], item[81],
                         item[82], item[83], item[84], item[85], item[86], item[87], item[88], item[89], item[90],
                         item[91], item[92], item[93], item[94], item[95], item[96]
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

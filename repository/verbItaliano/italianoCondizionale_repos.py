from .base_repos import PostgreDB
from models.verbItaliano.italianoCondizionale_model import Verbi, ItalianoOneVerb


class VerbiRepository:

    # <- Register a new 'Verb' in the table ->
    def New(self, infinitivoPresente='', condizionalePresenteIo='', condizionalePresenteTu='', 
            condizionalePresenteLui='', condizionalePresenteNoi='', condizionalePresenteVoi='', 
            condizionalePresenteLoro='', condizionalePassatoIo='', condizionalePassatoTu='', 
            condizionalePassatoLui='', condizionalePassatoNoi='', condizionalePassatoVoi='', 
            condizionalePassatoLoro=''):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.italiancondizionale (infinitivoPresente, condizionalePresenteIo, condizionalePresenteTu, " \
                     f"condizionalePresenteLui, condizionalePresenteNoi, condizionalePresenteVoi," \
                     f"condizionalePresenteLoro, condizionalePassatoIo, condizionalePassatoTu," \
                     f"condizionalePassatoLui, condizionalePassatoNoi, condizionalePassatoVoi, condizionalePassatoLoro)"\
                     f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            db.queryParams(insert, (
                infinitivoPresente, condizionalePresenteIo, condizionalePresenteTu, condizionalePresenteLui, 
                condizionalePresenteNoi, condizionalePresenteVoi, condizionalePresenteLoro, condizionalePassatoIo, 
                condizionalePassatoTu, condizionalePassatoLui, condizionalePassatoNoi, condizionalePassatoVoi, 
                condizionalePassatoLoro
            ))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List Verbs registered ->
    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.italiancondizionale")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Verb finder to redirect to the execution page ->
    def FindByVerb(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.italiancondizionale where infinitivoPresente = '{verbo}'")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List only the column "Verbo" ->
    def ListDistinctVerbs(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT DISTINCT infinitivoPresente FROM public.italiancondizionale")
            return self.__toListDistinctVerbs(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def Edit(self, infinitivoPresente='', condizionalePresenteIo='', condizionalePresenteTu='', 
            condizionalePresenteLui='', condizionalePresenteNoi='', condizionalePresenteVoi='', 
            condizionalePresenteLoro='', condizionalePassatoIo='', condizionalePassatoTu='', 
            condizionalePassatoLui='', condizionalePassatoNoi='', condizionalePassatoVoi='', 
            condizionalePassatoLoro=''):
        db = PostgreDB()
        try:
            updating_query = f"update public.italiancondizionale set infinitivoPresente=%s, condizionalePresenteIo=%s, condizionalePresenteTu=%s, condizionalePresenteLui=%s," \
                             f"condizionalePresenteNoi=%s, condizionalePresenteVoi=%s, condizionalePresenteLoro=%s, condizionalePassatoIo=%s," \
                             f"condizionalePassatoTu=%s, condizionalePassatoLui=%s, condizionalePassatoNoi=%s," \
                             f"condizionalePassatoVoi=%s, condizionalePassatoLoro=%s"
            db.queryParams(updating_query, (
                infinitivoPresente, condizionalePresenteIo, condizionalePresenteTu, condizionalePresenteLui,
                condizionalePresenteNoi, condizionalePresenteVoi, condizionalePresenteLoro, condizionalePassatoIo,
                condizionalePassatoTu, condizionalePassatoLui, condizionalePassatoNoi, condizionalePassatoVoi,
                condizionalePassatoLoro
            ))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete an user on DB ->
    def Delete(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.italiancondizionale WHERE infinitivoPresente = {verbo}")
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
                         item[10], item[11], item[12], item[13]
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
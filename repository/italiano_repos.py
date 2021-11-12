from .base_repos import PostgreDB
from models.italiano_model import Italiano, ItalianoOneVerb


class ItalianoRepository:

    # <- Register a new 'Verb' in the table ->
    def New(self, verbo, tempo, io, tu, lui, noi, voi, loro):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.italiano (verbo, tempo, io, tu, lui, noi, voi, loro)" \
                     f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            db.queryParams(insert, (verbo, tempo, io, tu, lui, noi, voi, loro))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List Verbs registered ->
    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.italiano")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Verb finder to redirect to the execution page ->
    def FindByVerb(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.italiano where verbo = '{verbo}'")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List only the column "Verbo" ->
    def ListDistinctVerbs(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT DISTINCT verbo FROM public.italiano")
            return self.__toListDistinctVerbs(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete an user on DB ->
    def Delete(self, verbo):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.italiano WHERE verbo = {verbo}")
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
            return Italiano(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
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
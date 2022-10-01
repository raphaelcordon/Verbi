from repository.base_repos import PostgreDB
from models.italiano_model import ItalianoOneVerb, Verbi


class inputVerbi:

    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.italiancondizionale")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

#select infinitivopresente, indicativopassatoprossimotu from public.verbi where indicativopassatoprossimoio = '';

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

'''
for item in inputVerbi().List():
    if item.indicativoPassatoProssimoTu[0:4] == 'hai ':
        #print(item.infinitivoPresente, item.indicativoPassatoProssimoTu)
        print(f"{item.infinitivoPresente} = hai {item.indicativoPassatoProssimoTu.split(' ', 1)[1]}")
        db = PostgreDB()
        try:
            db.query(
                f"update public.italiancondizionale "
                f"set infinitivopassato = 'avere {item.indicativoPassatoProssimoTu.split(' ', 1)[1]}', "
                f"participiopassato = '{item.indicativoPassatoProssimoTu.split(' ', 1)[1]}', "
                f"gerundiopassato = 'avendo {item.indicativoPassatoProssimoTu.split(' ', 1)[1]}' "
                )
        except Exception as exp:
            print(exp)
        finally:
            db.close()
        print(item.indicativoPassatoProssimoTu[3:])
'''

infinitivopresente = ['apparire', 'arrivare', 'cadere', 'consistere', 'costare', 'dipendere', 'diventare', 'dolere',
                      'emergere', 'entrare', 'esistere', 'essere', 'giacere', 'morire', 'nascere', 'parere',
                      'partire', 'piacere', 'rimanere', 'ritornare', 'riuscire', 'salire', 'scomparire', 'sedere',
                      'sorgere', 'stare', 'svanire', 'svenire', 'tornare', 'uscire', 'venire']

for item in infinitivopresente:
    if item[-3:] == 'ire':
        print(item[:-3])

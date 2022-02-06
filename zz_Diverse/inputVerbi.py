from repository.base_repos import PostgreDB
from models.italiano_model import ItalianoOneVerb, Verbi


class inputVerbi:

    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.verbi")
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


for item in inputVerbi().List():
    if item.indicativoPassatoProssimoTu[0:4] == 'hai ':
        #print(item.infinitivoPresente, item.indicativoPassatoProssimoTu)
        print(f"{item.infinitivoPresente} = hai {item.indicativoPassatoProssimoTu.split(' ', 1)[1]}")
        db = PostgreDB()
        try:
            db.query(f"update public.verbi set infinitivopassato = 'avere {item.indicativoPassatoProssimoTu.split(' ', 1)[1]}', participiopassato = '{item.indicativoPassatoProssimoTu.split(' ', 1)[1]}', gerundiopassato = 'avendo {item.indicativoPassatoProssimoTu.split(' ', 1)[1]}' where infinitivopresente = '{item.infinitivoPresente}'")
        except Exception as exp:
            print(exp)
        finally:
            db.close()
        print(item.indicativoPassatoProssimoTu[3:])

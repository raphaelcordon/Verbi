
class Italiano:
    def __init__(self,  id,  verbo,  tempo,  io,  tu,  lui,  noi,  voi,  loro):
        self.id = id
        self.verbo = verbo
        self.tempo = tempo
        self.io = io
        self.tu = tu
        self.lui = lui
        self.noi = noi
        self.voi = voi
        self.loro = loro


class ItalianoOneVerb:
    def __init__(self,  verbo):
        self.verbo = verbo


class Verbi:
    def __init__(self,  id, infinitivoPresente,
                 condizionalePresenteIo, condizionalePresenteTu, condizionalePresenteLui,
                 condizionalePresenteNoi, condizionalePresenteVoi, condizionalePresenteLoro,
                 condizionalePassatoIo, condizionalePassatoTu, condizionalePassatoLui,
                 condizionalePassatoNoi, condizionalePassatoVoi, condizionalePassatoLoro):
        self.id = id
        self.infinitivoPresente = infinitivoPresente
        self.condizionalePresenteIo = condizionalePresenteIo
        self.condizionalePresenteTu = condizionalePresenteTu
        self.condizionalePresenteLui = condizionalePresenteLui
        self.condizionalePresenteNoi = condizionalePresenteNoi
        self.condizionalePresenteVoi = condizionalePresenteVoi
        self.condizionalePresenteLoro = condizionalePresenteLoro
        self.condizionalePassatoIo = condizionalePassatoIo
        self.condizionalePassatoTu = condizionalePassatoTu
        self.condizionalePassatoLui = condizionalePassatoLui
        self.condizionalePassatoNoi = condizionalePassatoNoi
        self.condizionalePassatoVoi = condizionalePassatoVoi
        self.condizionalePassatoLoro = condizionalePassatoLoro

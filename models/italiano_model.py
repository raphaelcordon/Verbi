
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
    def __init__(self,  id, infinitivoPresente, infinitivoPassato, participioPresente, participioPassato,
                 gerundioPresente, gerundioPassato, indicativoPresenteIo, indicativoPresenteTu, indicativoPresenteLui,
                 indicativoPresenteNoi, indicativoPresenteVoi, indicativoPresenteLoro, indicativoPassatoProssimoIo,
                 indicativoPassatoProssimoTu, indicativoPassatoProssimoLui, indicativoPassatoProssimoNoi,
                 indicativoPassatoProssimoVoi, indicativoPassatoProssimoLoro, indicativoImperfettoIo,
                 indicativoImperfettoTu, indicativoImperfettoLui, indicativoImperfettoNoi, indicativoImperfettoVoi,
                 indicativoImperfettoLoro, indicativoTrapassatoProssimoIo, indicativoTrapassatoProssimoTu,
                 indicativoTrapassatoProssimoLui, indicativoTrapassatoProssimoNoi, indicativoTrapassatoProssimoVoi,
                 indicativoTrapassatoProssimoLoro, indicativoPassatoRemotoIo, indicativoPassatoRemotoTu,
                 indicativoPassatoRemotoLui, indicativoPassatoRemotoNoi, indicativoPassatoRemotoVoi,
                 indicativoPassatoRemotoLoro, indicativoTrapassatoRemotoIo, indicativoTrapassatoRemotoTu,
                 indicativoTrapassatoRemotoLui, indicativoTrapassatoRemotoNoi, indicativoTrapassatoRemotoVoi,
                 indicativoTrapassatoRemotoLoro, indicativoFuturoSempliceIo, indicativoFuturoSempliceTu,
                 indicativoFuturoSempliceLui, indicativoFuturoSempliceNoi, indicativoFuturoSempliceVoi,
                 indicativoFuturoSempliceLoro, indicativoFuturoAnterioreIo, indicativoFuturoAnterioreTu,
                 indicativoFuturoAnterioreLui, indicativoFuturoAnterioreNoi, indicativoFuturoAnterioreVoi,
                 indicativoFuturoAnterioreLoro, congiuntivoPresenteIo, congiuntivoPresenteTu, congiuntivoPresenteLui,
                 congiuntivoPresenteNoi, congiuntivoPresenteVoi, congiuntivoPresenteLoro, congiuntivoPassatoIo,
                 congiuntivoPassatoTu, congiuntivoPassatoLui, congiuntivoPassatoNoi, congiuntivoPassatoVoi,
                 congiuntivoPassatoLoro, congiuntivoImperfettoIo, congiuntivoImperfettoTu, congiuntivoImperfettoLui,
                 congiuntivoImperfettoNoi, congiuntivoImperfettoVoi, congiuntivoImperfettoLoro, congiuntivoTrapassatoIo,
                 congiuntivoTrapassatoTu, congiuntivoTrapassatoLui, congiuntivoTrapassatoNoi, congiuntivoTrapassatoVoi,
                 congiuntivoTrapassatoLoro, imperativoPresenteTu, imperativoPresenteLui, imperativoPresenteNoi,
                 imperativoPresenteVoi, imperativoPresenteLoro):
        self.id = id
        self.infinitivoPresente = infinitivoPresente
        self.infinitivoPassato = infinitivoPassato
        self.participioPresente = participioPresente
        self.participioPassato = participioPassato
        self.gerundioPresente = gerundioPresente
        self.gerundioPassato = gerundioPassato
        self.indicativoPresenteIo = indicativoPresenteIo
        self.indicativoPresenteTu = indicativoPresenteTu
        self.indicativoPresenteLui = indicativoPresenteLui
        self.indicativoPresenteNoi = indicativoPresenteNoi
        self.indicativoPresenteVoi = indicativoPresenteVoi
        self.indicativoPresenteLoro = indicativoPresenteLoro
        self.indicativoPassatoProssimoIo = indicativoPassatoProssimoIo
        self.indicativoPassatoProssimoTu = indicativoPassatoProssimoTu
        self.indicativoPassatoProssimoLui = indicativoPassatoProssimoLui
        self.indicativoPassatoProssimoNoi = indicativoPassatoProssimoNoi
        self.indicativoPassatoProssimoVoi = indicativoPassatoProssimoVoi
        self.indicativoPassatoProssimoLoro = indicativoPassatoProssimoLoro
        self.indicativoImperfettoIo = indicativoImperfettoIo
        self.indicativoImperfettoTu = indicativoImperfettoTu
        self.indicativoImperfettoLui = indicativoImperfettoLui
        self.indicativoImperfettoNoi = indicativoImperfettoNoi
        self.indicativoImperfettoVoi = indicativoImperfettoVoi
        self.indicativoImperfettoLoro = indicativoImperfettoLoro
        self.indicativoTrapassatoProssimoIo = indicativoTrapassatoProssimoIo
        self.indicativoTrapassatoProssimoTu = indicativoTrapassatoProssimoTu
        self.indicativoTrapassatoProssimoLui = indicativoTrapassatoProssimoLui
        self.indicativoTrapassatoProssimoNoi = indicativoTrapassatoProssimoNoi
        self.indicativoTrapassatoProssimoVoi = indicativoTrapassatoProssimoVoi
        self.indicativoTrapassatoProssimoLoro = indicativoTrapassatoProssimoLoro
        self.indicativoPassatoRemotoIo = indicativoPassatoRemotoIo
        self.indicativoPassatoRemotoTu = indicativoPassatoRemotoTu
        self.indicativoPassatoRemotoLui = indicativoPassatoRemotoLui
        self.indicativoPassatoRemotoNoi = indicativoPassatoRemotoNoi
        self.indicativoPassatoRemotoVoi = indicativoPassatoRemotoVoi
        self.indicativoPassatoRemotoLoro = indicativoPassatoRemotoLoro
        self.indicativoTrapassatoRemotoIo = indicativoTrapassatoRemotoIo
        self.indicativoTrapassatoRemotoTu = indicativoTrapassatoRemotoTu
        self.indicativoTrapassatoRemotoLui = indicativoTrapassatoRemotoLui
        self.indicativoTrapassatoRemotoNoi = indicativoTrapassatoRemotoNoi
        self.indicativoTrapassatoRemotoVoi = indicativoTrapassatoRemotoVoi
        self.indicativoTrapassatoRemotoLoro = indicativoTrapassatoRemotoLoro
        self.indicativoFuturoSempliceIo = indicativoFuturoSempliceIo
        self.indicativoFuturoSempliceTu = indicativoFuturoSempliceTu
        self.indicativoFuturoSempliceLui = indicativoFuturoSempliceLui
        self.indicativoFuturoSempliceNoi = indicativoFuturoSempliceNoi
        self.indicativoFuturoSempliceVoi = indicativoFuturoSempliceVoi
        self.indicativoFuturoSempliceLoro = indicativoFuturoSempliceLoro
        self.indicativoFuturoAnterioreIo = indicativoFuturoAnterioreIo
        self.indicativoFuturoAnterioreTu = indicativoFuturoAnterioreTu
        self.indicativoFuturoAnterioreLui = indicativoFuturoAnterioreLui
        self.indicativoFuturoAnterioreNoi = indicativoFuturoAnterioreNoi
        self.indicativoFuturoAnterioreVoi = indicativoFuturoAnterioreVoi
        self.indicativoFuturoAnterioreLoro = indicativoFuturoAnterioreLoro
        self.congiuntivoPresenteIo = congiuntivoPresenteIo
        self.congiuntivoPresenteTu = congiuntivoPresenteTu
        self.congiuntivoPresenteLui = congiuntivoPresenteLui
        self.congiuntivoPresenteNoi = congiuntivoPresenteNoi
        self.congiuntivoPresenteVoi = congiuntivoPresenteVoi
        self.congiuntivoPresenteLoro = congiuntivoPresenteLoro
        self.congiuntivoPassatoIo = congiuntivoPassatoIo
        self.congiuntivoPassatoTu = congiuntivoPassatoTu
        self.congiuntivoPassatoLui = congiuntivoPassatoLui
        self.congiuntivoPassatoNoi = congiuntivoPassatoNoi
        self.congiuntivoPassatoVoi = congiuntivoPassatoVoi
        self.congiuntivoPassatoLoro = congiuntivoPassatoLoro
        self.congiuntivoImperfettoIo = congiuntivoImperfettoIo
        self.congiuntivoImperfettoTu = congiuntivoImperfettoTu
        self.congiuntivoImperfettoLui = congiuntivoImperfettoLui
        self.congiuntivoImperfettoNoi = congiuntivoImperfettoNoi
        self.congiuntivoImperfettoVoi = congiuntivoImperfettoVoi
        self.congiuntivoImperfettoLoro = congiuntivoImperfettoLoro
        self.congiuntivoTrapassatoIo = congiuntivoTrapassatoIo
        self.congiuntivoTrapassatoTu = congiuntivoTrapassatoTu
        self.congiuntivoTrapassatoLui = congiuntivoTrapassatoLui
        self.congiuntivoTrapassatoNoi = congiuntivoTrapassatoNoi
        self.congiuntivoTrapassatoVoi = congiuntivoTrapassatoVoi
        self.congiuntivoTrapassatoLoro = congiuntivoTrapassatoLoro
        self.imperativoPresenteTu = imperativoPresenteTu
        self.imperativoPresenteLui = imperativoPresenteLui
        self.imperativoPresenteNoi = imperativoPresenteNoi
        self.imperativoPresenteVoi = imperativoPresenteVoi
        self.imperativoPresenteLoro = imperativoPresenteLoro


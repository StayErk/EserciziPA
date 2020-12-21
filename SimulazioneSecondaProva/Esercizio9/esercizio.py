"""
Esercizio numero sette slide esercizi2020
"""
import itertools
from collections import namedtuple
import time

class Observed:
    def __init__(self):
        self.observers = set()

    def add_observers(self, observer, *observers):
        for member in itertools.chain((observer,), observers):
            self.observers.add(member)
            member.update(None)

    def discard_observer(self, observer):
        self.observers.discard(observer)

    def notify(self, ob):
        for member in self.observers:
            member.update(ob)



class Libro(Observed):

    class RiferimentiDict(dict):

        oldSetItem = dict.__setitem__
        def __setitem__(self, key, value):
            raise RuntimeError

    def __init__(self, titolo: str, listaRiferimenti: list):
        super().__init__()
        self.riferimenti = Libro.RiferimentiDict()
        for count, riferimento  in enumerate(listaRiferimenti):
            self.riferimenti.oldSetItem(count, riferimento)

        self.titolo = titolo

        self._numero_copie = 0
        self._alta_progressione = False

    @property
    def numero_copie(self) -> int:
        return self._numero_copie

    @numero_copie.setter
    def numero_copie(self, value):
        oldNumeroCopie = self._numero_copie
        if self._numero_copie != value and self._numero_copie is not None:
            self._numero_copie = value
            self.notify(["numero_copie", self])
            if oldNumeroCopie*2 > self._numero_copie:
                self.alta_progressione = False
            elif oldNumeroCopie*2 <= self._numero_copie:
                self.alta_progressione = True

    @property
    def alta_progressione(self) -> bool:
        return self._alta_progressione

    @alta_progressione.setter
    def alta_progressione(self, value):
        self._alta_progressione = value
        self.notify(["alta_progressione", self])



class VistaIst:
    def update(self, ob):
        if ob == None: pass
        elif ob[0] == "numero_copie":
            print("Cambio stato: nuove vendite del libro \"{}\" per un totale di copie vendute pari a {} \n".format(ob[1].titolo, ob[1].numero_copie))
        elif ob[0] == "alta_progressione" and ob[1].alta_progressione:
            print("Cambio stato con l'ultimo acquisto, il libro \"{}\" ha più che raddoppiato le vendite\n".format(ob[1].titolo))
        elif ob[0] == "alta_progressione" and not ob[1].alta_progressione:
            print("Cambio stato: con l'ultimo acquisto, le venditedi \"{}\" sono aumentate meno della meta`\n".format(ob[1].titolo))

StoriaVendite = namedtuple("StoriaVendite", "titolo numerocopie tempo")
AndamentoVendite = namedtuple("AndamentoVendite", "stringa tempo")

class VistaStorica:

    def __init__(self):
        self.storia_vendite = []
        self.andamento_vendite = []

    def update(self, ob):
        if ob == None: pass
        elif ob[0] == "numero_copie":
            self.storia_vendite.append(StoriaVendite(ob[1].titolo, ob[1].numero_copie, time.time()))
        elif ob[0] == "alta_progressione" and ob[1].alta_progressione:
            self.andamento_vendite.append(AndamentoVendite("Raddoppio vendite di \"{}\"".format(ob[1].titolo), time.time()))
        elif ob[0] == "alta_progressione" and not ob[1].alta_progressione:
            self.andamento_vendite.append(AndamentoVendite("Incremento delle vendite di \"{}\" inferiore ad un mezzo del valore precedente".format(ob[1].titolo), time.time()))

    def storia(self) -> list:
        return [self.storia_vendite, self.andamento_vendite]

if __name__ == "__main__":
    vistaIst = VistaIst()
    vistaStorica = VistaStorica()
    libro1 = Libro("Guida Galattica Per Autostoppisti", ["Dizionario di Alieno", "Manuale Astronave", "Meccanica Quantistica per principianti"])
    libro2 = Libro("Python per esperti di Serpentese", ["Harry Potter e la Pietra Filosofale", "Le fiabe di Beda il Bardo", "Guida agli animali fantastici", "Python in practice"])
    libro1.add_observers(vistaIst, vistaStorica)
    libro2.add_observers(vistaIst, vistaStorica)

    libro1.numero_copie = 5
    libro2.numero_copie = 5

    libro1.numero_copie = 15
    libro2.numero_copie = 9

    print(vistaStorica.storia())
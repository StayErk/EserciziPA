"""
Esercizio 4 del 3 - 2- 2020
"""

import time
import datetime
from collections import namedtuple
import itertools

Tripla = namedtuple("Tripla", "nomeCorsolaurea votoMedio tempo")

class Observed:
    def __init__(self):
        self._observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self._observers.add(observer)
#            observer.update(None)

    def observers_discard(self, observer):
        self._observers.discard(observer)

    def observer_notify(self, ob):
        for observer in self._observers:
            observer.update(ob)


class CorsoDiLaurea(Observed):

    def __init__(self, nome, ultima_matricola):
        super().__init__()
        self._studenti = dict()
        self._mediaVotoLaurea = None
        self.flagMediaVotoLaurea = False
        self._mediaVotoLaureaOK = False
        self.flagMediaVotoLaureaOK = False
        self._numero_studenti = 0
        self.flagNumeroStudenti = 0
        self.nome = nome
        self.ultima_matricola = ultima_matricola



    @property
    def mediaVotoLaurea(self):
        return self._mediaVotoLaurea

    @mediaVotoLaurea.setter
    def mediaVotoLaurea(self, value: int):
        if self._mediaVotoLaurea != value:
            self._mediaVotoLaurea = value
            if self._mediaVotoLaurea > 100:
                self.mediaVotoLaureaOK = True
            else:
                self.mediaVotoLaureaOK = False
            self.observer_notify(["mediaVotoLaurea", self])

    @property
    def mediaVotoLaureaOK(self):
        return self._mediaVotoLaureaOK

    @mediaVotoLaureaOK.setter
    def mediaVotoLaureaOK(self, value: bool):
        if self._mediaVotoLaurea > 100 and self._mediaVotoLaureaOK is False:
            self._mediaVotoLaureaOK = value
            self.observer_notify(["mediaVotoLaureaOKTRUE", self])
        elif self._mediaVotoLaurea <= 100 and self._mediaVotoLaureaOK is True:
            self._mediaVotoLaureaOK = value
            self.observer_notify(["mediaVotoLaureaOKFALSE", self])

    @property
    def numero_studenti(self):
        return self._numero_studenti

    @numero_studenti.setter
    def numero_studenti(self, value: int):
        if self._numero_studenti != value:
            if self._numero_studenti < value:
                update = ["numeroStudentiAUM", self]
            elif self._numero_studenti > value:
                update = ["numeroStudentiDIM", self]
            self._numero_studenti = value
            self.observer_notify(update)

    @property
    def studenti(self):
        return self._studenti

    def addStudente(self, numeroMatricola, tuplaCognomeNome):
        self._studenti[numeroMatricola] = tuplaCognomeNome
        self.ultima_matricola = numeroMatricola
        self.numero_studenti += 1


    def removeStudente(self, numeroMatricola):
        self._studenti.pop(numeroMatricola)
        self.numero_studenti -= 1


class Segreteria:

    def update(self, model):
        if model[0] == "mediaVotoLaurea":
            print("Cambio stato: con l'ultima seduta di Laurea, il voto medio del Corso di Laurea in {} e` uguale a {}\n".format(model[1].nome, model[1].mediaVotoLaurea))
        elif model[0] == "mediaVotoLaureaOKTRUE":
                print("Cambio stato: con l'ultima seduta di Laurea, il voto medio del Corso di Laurea in {} e` diventatosuperiore a 100\n".format(model[1].nome))
        elif model[0] == "mediaVotoloLaureaOKFALSE":
                print("Cambio stato: con l'ultima seduta di Laurea, il voto medio del Corso di Laureain {} e` diventato minore o uguale di 100\n".format(model[1].nome))
        elif model[0] == "numeroStudentiAUM":
            print("Cambio stato: con le ultime immatricolazioni, il numero di studenti del Corso di Laurea in {} e` {}\n".format(model[1].nome, model[1].numero_studenti))
        elif model[0] == "numeroStudentiDIM":
            print("Cambio stato: con l’ultima seduta di Laurea, il numero di studenti del Corso di Laurea  {} e` {}\n".format(model[1].nome, model[1].numero_studenti))



class Storico:
    def __init__(self):
        self.listaTriple = []

    def update(self, model):
        if model[0] == "mediaVotoLaureaOKTRUE" or model[0] == "mediaVotoLaureaOKFALSE":
            self.listaTriple.append(Tripla(model[1].nome, model[1].mediaVotoLaurea, datetime.datetime.now()))

    def storia(self):
        return self.listaTriple


if __name__ == "__main__":
    segreteria = Segreteria()
    storico = Storico()

    corsoDL = CorsoDiLaurea("Informatica", "xlf123")
    corsoDL.observers_add(segreteria, storico)
    corsoDL.addStudente("xlf124", ("Ercolino", "Andrea"))
    corsoDL.addStudente("xlf125", ("Ercolino", "Pietro"))
    corsoDL.mediaVotoLaurea = 95
    corsoDL.mediaVotoLaurea = 110
    corsoDL.mediaVotoLaurea = 100
    corsoDL.removeStudente("xlf124")
    print(storico.storia())

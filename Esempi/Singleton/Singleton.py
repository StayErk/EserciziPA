#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Esempio di Design Pattern Singleton visto a lezione.

Il Singleton è un design patter creazionale ed è usato quando abbiamo
bisogno di una classa che ha un'unica istanza che è la sola ad essere
utilizzata dal programma. Utile in:
    controllare accesso concorrente a risorsa condivisa
    punto globale di accesso per la risorsa da parti differenti del sistema
    quando si ha bisogno di un unico oggetto di una certa classe
"""


class Singleton:

    class __impl:
        """ Implementa l'interfaccia del Singleton """

        def spam(self):
            """ Ritorna l'id del singleton, è un metodo di test 😐 """
            return id(self)

    # conserva il riferimento all'istanza.
    __instance = None

    def __init__(self):
        """
        Il costruttore si occupa di creare una singola istanza quindi:
        """

        # controlla se è già presente un'instanza dell'oggetto
        if Singleton.__instance is None:
            # Crea un istanza
            Singleton.__instance = Singleton.__impl()

        # conserva il riferimento all'instanza come singolo elemento in
        # __dict__

        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """ fa in modo che vengano invocati i metodi definiti in __impl """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ fa in modo che vengano invocati i metodi definiti in __impl """
        return setattr(self.__instance, attr, value)


if __name__ == "__main__":
    s1 = Singleton()
    print(id(s1), s1.spam())

    s2 = Singleton()
    print(id(s2), s2.spam())

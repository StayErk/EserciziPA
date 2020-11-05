#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""

class Classe:
    @classmethod
    def aggiungiMetodo(cls, funzione = None):
        if not funzione is None and callable(funzione):
            cls.f = funzione

if __name__ == "__main__":

    def stampa4():
        print('4')

    Classe.aggiungiMetodo(stampa4)

    Classe.f()

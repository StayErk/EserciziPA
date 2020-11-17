#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""
from functools import wraps


def coroutine(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        generatore = function(*args, **kwargs)
        next(generatore)
        return generatore
    return wrapper


@coroutine
def gestore_lett(successore=None):
    while True:
        stringa = yield
        if stringa[0].isalpha():
            print("Richiesta {} gestita da gestore_lett".format(stringa))
        elif successore is not None:
            successore.send(stringa)

@coroutine
def gestore_num(successore=None):
    while True:
        stringa = yield
        if stringa[0].isdigit():
            print("Richiesta {} gestita da gestore_num".format(stringa))
        elif successore is not None:
            successore.send(stringa)

@coroutine
def gestore_und(successore=None):
    while True:
        stringa = yield
        if stringa.startswith('_'):
            print("Richiesta {} gestita da gestore_und".format(stringa))
            pipeline = gestore_num(gestoreDiDefault(gestore_lett(gestore_und())))
            pipeline.send(stringa[1:])
        elif successore is not None:
            successore.send(stringa)

@coroutine
def gestoreDiDefault(successore= None):
    while True:
        stringa = yield
        if not (stringa[0].isalpha() or stringa[0].isdigit() or stringa.startswith('_')):
            print("Messaggio da GestoreDiDefault: Non è stato possibile gestire la richiesta {}".format(stringa))
        elif successore is not None:
            successore.send(stringa)

def richieste(lst):
    pipeline = gestore_lett(gestore_num(gestoreDiDefault(gestore_und())))

    for stringa in lst:
        pipeline.send(stringa)

if __name__ == "__main__":
    lst = ["ciao", "1base", "_vita", "default", "!nonGestibile"]

    richieste(lst)


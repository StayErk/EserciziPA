#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Soluzione proposta dalla professoressa
"""
from functools import wraps

def decora(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        out = ''
        # perché non usare kwargs.value() ?
        for arg in args + tuple(v for k,v in kwargs.items()):
            if type(arg) != str:
                raise TypeError
            out += arg+" "
        result = str(function(*args, ** kwargs))
        out += result
        return out
    return wrapper

def decora2(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        out = ''
        # provo a usare kwargs.value() ?
        for arg in args + tuple(kwargs.values()):
            if type(arg) != str:
                raise TypeError
            out += arg+" "
        result = str(function(*args, ** kwargs))
        out += result
        return out
    return wrapper


if __name__ == "__main__":

    print("Definisco la funzione ciao decorata con @decora. La funzione ciao restituisce il risultato di 2 + 2")

    @decora2
    def ciao(*args, **kargs):
        return 2 + 2

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 'stai'. Mi aspetto: 'ciao come stai? 4'")
    ciao("ciao", "come", "stai?")

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 3. Mi aspetto: Type Error")
    try:
        ciao("ciao", "come", 3)
    except TypeError:
        print("Type Error catturato")

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 'stai?' e "
          "parametro keyword key = 3. Mi aspetto: Type Error")
    try:
        ciao("ciao", "come", "stai?", key=3)
    except TypeError:
        print("Type Error catturato")

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 'stai?' e "
          "parametro keyword key = '3'. Mi aspetto: 'Ciao come stai? 3 4'")
    ciao("ciao", "come", "stai?", key="3")

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


def defc(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs.items()) > 2:
            raise TypeError
        else:
            frisultati = open("risultato.txt", 'a')
            risultatoFunzione = function(*args, **kwargs)
            if not risultatoFunzione is None:
                frisultati.write(str(risultatoFunzione))
            if len(args) > 0:
                frisultati.write(str(args[0]))
            else:
                frisultati.write(str(next(iter(kwargs.values()))))
            frisultati.write('\n')
            frisultati.close()
    return wrapper


def defc2(maxArgs = None):
    if maxArgs is None:
        maxArgs = 2
    def defc(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if len(args) + len(kwargs.items()) > maxArgs:
                raise TypeError
            else:
                frisultati = open("risultato.txt", 'a')
                risultatoFunzione = function(*args, **kwargs)
            if not risultatoFunzione is None:
                frisultati.write(str(risultatoFunzione))
            if len(args) > 0:
                frisultati.write(str(args[0]))
            else:
                frisultati.write(str(next(iter(kwargs.values()))))
            frisultati.write('\n')
            frisultati.close()
        return wrapper
    return defc




if __name__ == "__main__":
    @defc2(2)
    def funzione1(*args, **kwargs):
        return 2 + 2

    @defc2(3)
    def funzione2(*args, **kwargs):
        pass

    print("Chiamo funzione1 con tre argomenti. Mi aspetto typeerror")
    try:
        funzione1('ciao', 'andrea', 1)
    except TypeError:
        print('TypeError lanciato')

    print("Chiamo funzione1 con due argomenti posizionali, ciao e piccibu. Nel file mi aspetto 4 e ciao")
    funzione1('ciao', 'piccibu')
    f_i = open('risultato.txt', 'r')
    print(f_i.read())

    print("Chiamo funzione1 con un argomento keyword con valore ipse dixit. Nel file mi aspetto 4 e ipse dixit")
    funzione1(disse='ipse dixit')
    print(f_i.read())

    print("Chiamo funzione2 con tre argomenti. Mi aspetto typeerror")
    try:
        funzione2('ciao', 'andrea', 1)
    except TypeError:
        print('TypeError lanciato')

    print("Chiamo funzione2 con due argomenti posizionali, ciao e piccibu. Nel file mi aspetto ciao")
    funzione2('ciao', 'piccibu')
    print(f_i.read())

    print("Chiamo funzione1 con un argomento keyword con valore ipse dixit. Nel file mi aspetto ipse dixit")
    funzione2(disse='ipse dixit')
    print(f_i.read())

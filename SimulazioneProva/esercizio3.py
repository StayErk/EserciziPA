#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Definire un decoratore di funzione che trasforma una funzione che prende in input un numero variabile di numeri in una fuzione che prende in input una lista e opera solo sugli elementi della lista di tipo float, int e str convertiti in int
"""

from functools import wraps

def decoratore(function):
    @wraps(function)
    def wrapper(l, *args, **kwargs):
        if l and isinstance(l, list):
            lst = []
            for item in l:
                if (isinstance(item, str)):
                    lst.append(int(item))
                elif (isinstance(item, (float, int))):
                    lst.append(item)
            somma = function(*lst)
            return somma
    return wrapper
            

@decoratore
def somma(*args):
    """
    Prende un numero variabile di numeri e li somma
    """
    somma = 0
    for n in args:
        if(isinstance(n, (float, int))):
            somma += n
    return somma


a = somma([1, 3, 1, "5"])
print(a)

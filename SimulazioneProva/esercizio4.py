#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Modificare la funzione al punto precedente in modo che la funzione decorata operi su qualsiasi elemento
possa essere convertito in int e che non si abbia errore se un elemento della lista non può essere convertito a int anche se è 
di un tipo convertibile a int

"""

from functools import wraps

def decoratore(function):
    @wraps(function)
    def wrapper(l, *args, **kwargs):
        if l and isinstance(l, list):
            lst = []
            for item in l:
                if isinstance(item, str):
                    try:
                        lst.append(int(item))
                    except ValueError:
                        pass
                elif isinstance(item, (float, int)):
                    lst.append(item)
            return function(*lst)
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

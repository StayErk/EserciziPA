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

def decFact(numberOfArgs = None):

    if numberOfArgs is None: raise AttributeError

    def decorator(cls):

        # questa funzione rappresenta il decoratore di funzione che deve essere agganciato alla classe decorata
        def decoratoreDiFunzione(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                if len(args) + len(kwargs.values()) != numberOfArgs:
                    raise TypeError
                risultatoFunzione = function(*args, **kwargs)
                f_o = open('risultat.txt', 'a')
                if not risultatoFunzione is None:
                    f_o.write(str(risultatoFunzione))
                if len(args) > 0:
                    f_o.write(str(args[0]))
                else:
                    f_o.write(str(next(iter(kwargs.items()))))
                f_o.write("\n")
                f_o.close()
            return wrapper

        cls.decoratore = decoratoreDiFunzione
        return cls
    return decorator

@decFact(2)
class aClass1:
    pass


if __name__ == "__main__":

    @aClass1.decoratore
    def funzioneProva(*args, **kwargs):
        print("ho usato il numero corretto di argomenti")

    try:
        funzioneProva("ciao")
    except TypeError:
        print("funzione 1 ha lanciato TypeError")

    funzioneProva("ciao", "hello")  

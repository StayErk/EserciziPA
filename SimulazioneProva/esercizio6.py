#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo per contare 
il numero di invocazioni del metodo passato al decorator factory
"""
from functools import wraps

def decoratorFactory(nomeMetodo):
    def decoratore(cls):
        cls._contatoreChiamate = 0

        @property
        def contatoreChiamate(self):
            return self._contatoreChiamate
        
        setattr(cls, 'contatoreChiamate', contatoreChiamate)
        oldMetodo = getattr(cls, nomeMetodo)

        def newMetodo(self, *args, **kwargs):
            self._contatoreChiamate += 1
            return oldMetodo(self, *args, **kwargs)

        setattr(cls, nomeMetodo, newMetodo)
        return cls
    return decoratore


@decoratorFactory('metodoDaContare')
class aClass:
    
    def metodoDaContare(self):
        print('ciao')
            
            
a = aClass()

a.metodoDaContare()
a.metodoDaContare()
a.metodoDaContare()
a.metodoDaContare()
a.metodoDaContare()
print(a.contatoreChiamate)

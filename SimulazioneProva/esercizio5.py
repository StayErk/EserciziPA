#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Scrivere una classe di base ClsBasein cui c'è un metodo addAttr che controlla se la classe ha l'attributo di nome s e se tale non è presente 
allora aggiunge l'attributo s con valore v, in caso contrario non fa niente. Il metodo deve funzionare anche nelle sottoclassi
"""

class ClsBase:

    @classmethod
    def addAttr(cls):
        if 's' not in cls.__dict__.keys():
            print('aggiunto v a {}'.format(cls.__name__))
            cls.s = 'v'

class ClsDue(ClsBase):
    pass

class ClsTre(ClsBase):
    def __init__(self):
        self._s = "Io ho definito l'attributo s"

    @property
    def s(self):
        return self._s



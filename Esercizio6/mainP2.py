#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""
def decoratore(cls):
    if not 'ff' in cls.__dict__.keys() or not callable(cls.__dict__['ff']):
        ClasseConFF.ff()
    return cls

class ClasseConFF():
    @classmethod
    def ff(cls):
        print("Il decoratore mi ha invocato")

@decoratore
class ConFF():
    def ff(self):
        print('hello')

@decoratore
class SenzaFF():
    def ae(self):
        print (2 + 2)

if __name__ == "__main__":
    f = ConFF()
    f.ff()

    s = SenzaFF()


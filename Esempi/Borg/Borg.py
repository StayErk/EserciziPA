#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Nella classe borg tutte le istanze sono diverse ma condividono lo stesso stato
"""

class Borg:
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class Child(Borg):
    pass

if __name__ == "__main__":
    borg = Borg()
    another_borg = Borg()

    # Le due variabili puntano a due riferimenti diversi in memoria.
    print(borg is  another_borg)

    child = Child()
    borg.only_one_var = "i'm the only one var"

    # Ma condividono lo stesso stato.
    print(child.only_one_var)

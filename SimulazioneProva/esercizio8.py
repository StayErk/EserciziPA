#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Scrivere una classe le cui istanze possono avere un'unica variabile di instanza di nome unica
"""

class ClasseConUnica:
    class _unica:
        
        def __init__(self) -> None:
            self.unica = "unica"
            

    def __init__(self) -> None:
        self.__dict__['_impl'] = ClasseConUnica._unica()

    def __getattr__(self, name: str) -> any:
        if name == "unica":
            return getattr(self._impl, name)

    def __setattr__(self, name: str, value: any) -> None:
        if name == "unica":
            return setattr(self._impl, name, value)

a = ClasseConUnica()

print(a.unica)
a.ciao = 'hella'

print(a.ciao, a.__dict__.values())

a.unica = "ciao"
print(a.unica)

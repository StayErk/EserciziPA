#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Scrivere un decoratore di classe che, se applicato ad una classe la modifica
in modo che funzioni come se fosse stata derivata dalla seguente classe base:

class ClassBase:
    varC = 1000
    def __init__(self):
        self.varl = 10

    def f(self, v):
        print(v*self.varl)

    @staticmethod
    def g(x):
        print(x * varC)
"""


def classBase(Class):
    setattr(Class, "varC", 1000)

    def newInit(self):
        self.varl = 10
    setattr(Class, "__init__", newInit)

    def f(self, v):
        print(v * self.varl)
    setattr(Class, "f", f)

    def g(x):
        print(x * Class.varC)

    g = staticmethod(g)
    setattr(Class, "g", g)

    return Class


@classBase
class C:
    pass

if __name__ == "__main__":
    c = C()
    print(c.varl)
    c.f(15)
    C.g(15)

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Non funziona (?)
"""
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """ sono la proprietà 'x'"""
        return self._x

    @x.setter
    def setx(self, value):
        self._x = value

    @x.deleter
    def delx(self):
        del self._x


c = C()

c.setx('Hello')
print(c.x())
c.delx()
print(c.x())

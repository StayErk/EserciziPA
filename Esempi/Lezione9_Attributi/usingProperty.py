#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""

class C:
    def __init__(self):
        self._x = None

    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x

    # L'ultima stringa rappresenta la docstring della proprietà
    x = property(getx, setx, delx, "sono la proprietà 'x'")


c = C()

c.setx('Hello')
print(c.getx())
c.delx()
print(c.getx())

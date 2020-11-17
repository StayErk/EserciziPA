#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Creare un generatore che stampi uno ad uno gli elementi di una lista al contrario
"""

def generatore(lista):
    if len(lista) > 0:
        yield lista[len(lista) -1]
        yield from generatore(lista[:len(lista) -1])



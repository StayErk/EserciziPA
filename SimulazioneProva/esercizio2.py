#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Scrivere una funzione generatrice che prende in input un intero positivo n e restituisce un iteratore degli interi 0,1,3,6. Somma di n positivi
"""

def sommaInteri(n):
    somma = 0
    if n > 0:
        for i in range(n):
            somma += i
            yield somma

generatore = sommaInteri(10)

for i in range(10):
    print(next(generatore))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Esercizio 4 appello del 18 febbraio 2020
"""

from concurrent.futures import ProcessPoolExecutor

def creaDizionari(listaInteri: list, concurrency: int):
    futures = set()
    with ProcessPoolExecutor(max_workers=concurrency) as executor:
        for intero in get_jobs(listaInteri):
            future = executor.submit(creaDizionario, intero)
            futures.add(future)
        wait_for(futures)


def get_jobs(listaInteri):
    for i in listaInteri:
        yield i

def creaDizionario(intero: int):
    pass

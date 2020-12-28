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

import concurrent.futures
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

def wait_for(futures: set):
    canceled = False
    try:
        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is None:
                result = future.result()
                print("Creato il dizionario {}. Con parametro intero: {}".format(result[0], result[1:]))
            else:
                raise err
    except KeyboardInterrupt:
        print("cancellato dall'utente")
        canceled = True
        for future in futures:
            future.cancel()
    return (len(futures), result, canceled)

def creaDizionario(intero: int):
    dict = {}
    for i in range(intero):
        dict[i+1] = i+1 + intero
    return dict, intero


if __name__ == "__main__":
    creaDizionari([1, 2, 4 ,6 ,9, 2, 1], 2)

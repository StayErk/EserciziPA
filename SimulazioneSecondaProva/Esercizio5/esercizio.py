#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""
from multiprocessing import JoinableQueue, Queue, Process

def cerca(listaParole: list, listaDiFile: list, concurrency: int):
    jobs = JoinableQueue()
    results = Queue()
    # creare i processi
    create_processes(jobs, results, concurrency)
    # creare i jobs e metterli in todo
    add_jobs(listaDiFile, listaParole, jobs)
    jobs.join()

    while not results.empty():
        result = results.get_nowait()
        print("JOB: {} la parola {} compare di più nel file {}".format(result[0], result[1], listaDiFile[result[0]]))

def create_processes(jobs: JoinableQueue, results: Queue, concurrency: int):
    for _ in range(concurrency):
        process = Process(target=worker, args=(jobs, results))
        process.daemon = True
        process.start()

def worker(jobs: JoinableQueue, results: Queue):
    while True:
        indiceFile, nomeFile, listaParole = jobs.get()
        result = cercaParola(nomeFile, listaParole)
        results.put((indiceFile, result))
        jobs.task_done()


def cercaParola(nomeFile: str, listaParole: list) -> str:
    f_i = open(nomeFile, 'r')
    text = f_i.read()
    words = text.split()
    counterDict = {}
    for singolaParola in listaParole:
        counterDict[singolaParola] = 0

    for word in words:
        for singolaParola in listaParole:
            if word == singolaParola:
                counterDict[singolaParola] += 1

    print(counterDict)
    parolaMax = max(counterDict, key=counterDict.get)
    return parolaMax

def add_jobs(listaDiFile: list, listaDiParole: list, jobs: JoinableQueue):
    for todo, name in enumerate(listaDiFile):
        jobs.put((todo, name, listaDiParole))


if __name__ == "__main__":
    nomiFile = ["t1.txt", "t2.txt", "t3.txt", "t4.txt", "t5.txt"]
    listaParole = ["asparago", "martinucci", "patata", "agglomerato", "sambuca", "approccio", "correttezza"]
    
    cerca(listaParole, nomiFile, 3)

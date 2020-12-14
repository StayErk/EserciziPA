#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""
from collections import namedtuple
from multiprocessing import JoinableQueue, Queue, Process
import os
import sys
import time
# La tupla Result e' composta in modo che (1,0, <name>) indichi un file copiato senza modifiche e (0,1,<name>) uno trascritto con modifiche
Result = namedtuple("Result", "copied scaled name")
Summary = namedtuple("Summary", "todo copied scaled canceled")

def main():
    try:
        lettera, source, target, concurrency = handle_commandline()
    except TypeError:
        return
    print("Starting...")
    start = time.time()
    summary = copy(lettera, source, target, concurrency)
    summarize(summary, concurrency)
    end = time.time()
    total = end - start
    print(total)

def handle_commandline() -> tuple:
    """
    Si occupa di prelevare gli argomenti da linea di comando e di farne il cast al tipo esatto
    """
    if len(sys.argv) != 5:
        print("Numero argomenti errato:\n\t<c>: lettera da cancellare\n\t<pathSource>\n\t<pathTarget>\n\t<#processi>")
        return 
    argomenti = (sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
    return argomenti

def copy(lettera, source, target, concurrency):
    """
    Metodo core della parte multiprocessing.
    """
    canceled = False
    # Creo una coda di processi joinable a cui assegnare i job
    jobs = JoinableQueue() 
    # Coda dei risultati
    results = Queue()

    create_processes(lettera, jobs, results, concurrency)
    todo = add_jobs(source, target, jobs)

    try:
        jobs.join()
    except KeyboardInterrupt:
        print("Interrotto dall'utente")
        canceled = True

    copiati = trascritti = 0

    while not results.empty():
        result = results.get_nowait()
        copiati += result.copied
        trascritti += result.scaled
    return Summary(todo, copiati, trascritti, canceled)

def create_processes(lettera, jobs, results, concurrency):
    #per ogni core creo un processo che eseguira' il metodo worker con lista dei jobs: jobs
    for _ in range(concurrency):
        process = Process(target=worker, args=(lettera, jobs, results))
        process.daemon = True
        process.start()

def worker(lettera, jobs, results):
    """
    Il metodo worker si occupa di prelevare un job dalla coda e di eseguirlo,
    infine marca il job terminato con jobs.task_done()
    """
    while True:
        try:
            sourceFile, targetFile = jobs.get()
            try:
                result = copia_uno(lettera, sourceFile, targetFile)
                print("{} {}".format("copiato" if result.copied else "trascritto", os.path.basename(result.name)))
                results.put(result)
            except FileNotFoundError as err:
                print(str(err))
        finally:
            jobs.task_done()

def add_jobs(source, target, jobs):
    """
    Questo metodo si occupa di inserire all'interno della lista dei job il la tupla sourceFile e targetFile
    che saranno usati nel metodo copia_uno per lavorare sul file
    """
    for todo, name in enumerate(os.listdir(source), start=1):
        sourceFile = os.path.join(source, name)
        targetFile = os.path.join(target, name)
        jobs.put((sourceFile, targetFile))
    return todo

def copia_uno(lettera, sourceFile, targetFile):
    """
    Questo metodo ha lo scopo di aprice il file con path sourceFile e di copiare il suo contenuto nel file con path targetFile 
    in modo che se il testo nel file contenuto in sourceFile contenga la lettere indicata come argomento del programma il testo di output non la contenga
    in caso contrario copia il file per intero
    """
    vecchioFile = open(sourceFile, "r")
    text = vecchioFile.read()
    newText = ""
    if text.count(lettera) == 0:
        nuovoFile = open(targetFile, "w")
        nuovoFile.write(text)
        nuovoFile.close()
        # Indica che il file e' stato copiato
        return Result(1, 0, targetFile)
    else:
        for c in text:
            if c.lower() != lettera.lower():
                newText += c
        nuovoFile = open(targetFile, "w")
        nuovoFile.write(newText)
        nuovoFile.close()
        # indica che il file e' stato trascritto
        return Result(0, 1, targetFile)

def summarize(summary, concurrency):
    message = "copied {} scaled {}".format(summary.copied, summary.scaled)
    difference = summary.todo - (summary.copied + summary.scaled)
    if difference:
        message += " skipped {} ".format(difference)
    message += " using {} processes ".format(concurrency)
    if summary.canceled:
        message + " [canceled]"
    print(message)


if __name__ == "__main__":
    main()

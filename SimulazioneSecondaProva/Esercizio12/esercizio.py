"""
Esercizio 4 dell'appello del 18 febbraio 2020
"""

from concurrent import futures
def creaDizionari(listaInteri, concorrenza):
    futuri = set()
    with futures.ProcessPoolExecutor(max_workers=concorrenza) as executor:
        for index, intero in get_jobs(listaInteri):
            process = executor.submit(creaDizionario, index, intero)
            futuri.add(process)

        wait_for(futuri)

def get_jobs(listaInteri):
    for count, intero in enumerate(listaInteri,start=1):
        yield count, intero

def creaDizionario(index, intero):
    d = {}
    for i in range(intero):
        d[i] = i + index
    return d, index

def wait_for(futuri):
    for future in futures.as_completed(futuri):
        err = future.exception()
        if err is None:
            print(sum(future.result()[0].values()), future.result()[1])



if __name__ == "__main__":
    creaDizionari([3, 2, 1], 3)
from concurrent.futures import process, ProcessPoolExecutor
import math
import concurrent
def creaListe(listaDiStringhe: list, n: int, concurrency):
    futures = set()
    listeOutput = []
    with ProcessPoolExecutor(max_workers=concurrency) as executor:
        for count, string in get_jobs(listaDiStringhe):
            future = executor.submit(creaSingolaLista, string, n, count)
            futures.add(future)
        print(wait_for(futures))

def get_jobs(listaDiStringhe):
    for count, string in enumerate(listaDiStringhe):
        yield (count, string)

def creaSingolaLista(string, n, count):
    l = []
    size = n // (10**count)
    print(size, n, count, 10**count)
    for i in range(size):
        l.append(string)

    return l

def wait_for(futures):
    listaDiListe = []
    for future in concurrent.futures.as_completed(futures):
        listaDiListe.append(future.result())

    return listaDiListe


if __name__ == "__main__":
    creaListe(["ciao", "andrea", "pollo"], 5000, 3)
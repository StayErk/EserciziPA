from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

def creaDizionari(listaInteri, concorrenza):
    futuri = set()
    with ThreadPoolExecutor(concorrenza) as executor:
        for count, intero in get_jobs(listaInteri):
            future = executor.submit(creaDizionario, count, intero)
            futuri.add(future)
        wait_for(futuri)

def get_jobs(listaInteri):
    for index, intero in enumerate(listaInteri, start=1):
        yield (index, intero)

def creaDizionario(count, intero):
    d = {}
    for i in range(intero):
        d[i] = i + count

    return d, count


def wait_for(futuri):
    try:
        for futuro in futures.as_completed(futuri):
            errore = futuro.exception()
            if errore is None:
                result = futuro.result()
                print(sum(result[0].values()), result[1])
    except RuntimeError:
        print("Verificata eccezione")
    finally:
        print("terminato")

if __name__ == "__main__":
    creaDizionari([3, 2, 1], 3)


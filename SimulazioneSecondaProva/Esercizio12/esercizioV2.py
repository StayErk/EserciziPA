from threading import Thread
from queue import Queue

def creaDizionari(listaInteri, concorrenza):
    jobs = Queue()
    results = Queue()

    create_threads(jobs, results, concorrenza)
    add_jobs(listaInteri, jobs)
    process(jobs, results)

def create_threads(jobs, results, concorrenza):
    for _ in range(concorrenza):
        thread = Thread(target=worker, args=(jobs, results), daemon=True)
        thread.start()

def add_jobs(listaInteri, jobs):
    for count, intero in enumerate(listaInteri, start=1):
        jobs.put((count, intero))

def worker(jobs, results):
    while True:
        try:
            count, intero = jobs.get()
            result = creaDizionario(count, intero)
            results.put(result)
        finally:
            jobs.task_done()

def creaDizionario(count, intero):
    d = {}
    for i in range(intero):
        d[i] = i + count
    return d, count

def process(jobs, results):
    try:
        jobs.join()
        while not results.empty():
            result = results.get()
            print(sum(result[0].values()), result[1])
    finally:
        print("terminato")



if __name__ == "__main__":
    creaDizionari([3, 2, 1, 5], 3)


from threading import Thread
from queue import Queue
def creaListe(listaDiStringhe: list, n: int, concurrency: int):
    jobs = Queue()
    results = Queue()

    create_threads(jobs, results, concurrency)
    add_jobs(jobs, listaDiStringhe, n)
    process(jobs, results)

def add_jobs(jobs, listaDiStringhe, n):
    for count, string in enumerate(listaDiStringhe):
        jobs.put((string, n // 10 ** count))

def create_threads(jobs, results, concurrency):
    for _ in range(concurrency):
        thread = Thread(target=worker, args=(jobs, results), daemon=True)
        thread.start()

def worker(jobs, results):
    while True:
        try:
            stringaDaInserire, size = jobs.get()
            result = creaListaSingola(stringaDaInserire, size)
            results.put(result)
        finally:
            jobs.task_done()

def creaListaSingola(stringa, size):
    l = []
    for _ in range(size):
        l.append(stringa)
    return l

def process(jobs, results):
    jobs.join()
    while not results.empty():
        result = results.get_nowait()
        print(result)

if __name__ == "__main__":
    creaListe(["ciao", "andrea", "pollo"], 5000, 3)
from  multiprocessing import Process, Queue, JoinableQueue

def creaListe(listaDiStringhe, n, concurrency):
    jobs = JoinableQueue()
    results = Queue()
    create_processes(jobs, results, concurrency)
    todo = add_jobs(listaDiStringhe, n, jobs)
    jobs.join()
    while not results.empty():
        print(results.get_nowait())

def create_processes(jobs, results, concurrency):
    for _ in range(concurrency):
        process = Process(target=worker, args=(jobs, results), daemon=True)
        process.start()
        
        
def add_jobs(listaDiStringhe, n, jobs):
    for count, stringa in enumerate(listaDiStringhe):
        jobs.put((stringa, n // 10 ** count))

def worker(jobs, results):
    while True:
        try:
            stringaDaInserire, sizeLista = jobs.get()
            result = creaListaSingola(stringaDaInserire, sizeLista)
            results.put(result)
        finally:
            jobs.task_done()


def creaListaSingola(stringa, size):
    l =[]
    for _ in range(size):
        l.append(stringa)
    return l



if __name__ == "__main__":
    creaListe(["ciao", "andrea", "pollo"], 5000, 3)
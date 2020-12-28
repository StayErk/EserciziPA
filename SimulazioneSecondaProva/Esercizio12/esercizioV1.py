from multiprocessing import JoinableQueue, Queue, Process

def creaDizionari(listaInteri, concorrenza):
    jobs = JoinableQueue()
    results = Queue()
    create_processes(concorrenza, jobs, results)
    add_jobs(listaInteri, jobs)
    jobs.join()
    while not results.empty():
        result = results.get()
        print(sum(result[0].values()), result[1])

def add_jobs(listaInteri, jobs):
    for count, intero in enumerate(listaInteri, start=1):
        jobs.put((count, intero))

def create_processes(concorrenza, jobs, results):
    for _ in range(concorrenza):
        process = Process(target=worker, args=(jobs, results), daemon=True)
        process.start()

def worker(jobs, results):
    while True:
        try:
            index, intero = jobs.get()
            result = creaDizionario(index, intero)
            results.put(result)
        finally:
            jobs.task_done()

def creaDizionario(index, intero):
    d = {}
    for i in range(intero):
        d[i] = i + index

    return d, index

if __name__ == "__main__":
    creaDizionari([3, 2, 1], 3)
"""
Esercizio 8 delle slide esericizidicembre2020
"""

from functools import wraps

def coroutine(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        generatore = function(*args, **kwargs)
        next(generatore)
        return generatore
    return wrapper

@coroutine
def handler_04(successor = None):
    while True:

        richiesta = yield

        if 0 <= richiesta[0] <= 4:
            print("Richiesta {} gestita da Handler_04".format(richiesta))
        elif successor is not None:
            successor.send(richiesta)

@coroutine
def handler_59(successor = None):
    while True:
        richiesta = yield 
        if 5 <= richiesta[0] <= 9:
            print("Richiesta {} gestita da Handler_59".format(richiesta))
        elif successor is not None:
            successor.send(richiesta)

@coroutine
def handler_gt9(successor = None):
    while True:
        richiesta = yield
        if richiesta[0] > 9:
            print("Messaggio da handler_gt9: non è stato possibile gestire la richiesta {}. Richiesta modificata".format(richiesta))
            richiesta[0] = richiesta[0] - richiesta[1]
            pipeline = handler_04(handler_59(handler_gt9(default_handler())))
            pipeline.send(richiesta)
        elif successor is not None:
            successor.send(richiesta)

@coroutine
def default_handler(successor = None):
    while True:
        richiesta = yield
        if richiesta[0] < 0 or  \
            not (isinstance(richiesta[0], int) and isinstance(richiesta[0], int)) or \
            len(richiesta) > 2:
            
            print("Richiesta {} gestita da Default_handler: non è stato possibile gestire la richiesta {}".format(richiesta, richiesta))


def inviaRichieste(listaDiRichieste: list):
    pipeline = handler_04(handler_59(handler_gt9(default_handler())))
    for richiesta in listaDiRichieste:
        pipeline.send(richiesta)


if __name__ == "__main__":
    l = [[1, 3], [5, 4], [3, 2], [-1, 7], [10, 5]]

    print("\nhandler0-4, handler5-9, handler0-4, default, handlergt-9, handler5-9")
    inviaRichieste(l)
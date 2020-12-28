"""
I contenxt manager consentono di allocare e rilasciare risorse quando vogliamo.
Lo statement with è l'esempio più usato di context manager
"""


"""
Implementazioe context manager con classe. Sovrascrivere i metodi:
 * __init__
 * __enter__
 * __exit__
"""

class File:
    def __init__(self, file_name: str, method: str):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    """
    Il metodo __exit__ potrebbe gestire anche una possibile eccezione invocata
    tra il metodo enter e exit. Se exit restituisce true allora l'eccezione non viene 
    lanciata dallo statement with altrimenti viene lanciata anche dallo statement with
    """

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


"""
Implementazione attraverso decoratore
"""

from contextlib import contextmanager


"""
Per gestire un'eccezione basta inserire yield e close all'interno di uno 
statement try finally. 
"""
@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    yield f
    f.close()

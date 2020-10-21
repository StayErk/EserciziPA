from functools import wraps

def decora(function):
    @wraps(function)
    def wrapper(*args, **kargs):
        concatenation = ''
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError
            else:
                concatenation += arg + " "

        for karg in kargs.values():
             if not isinstance(karg, str):
                raise TypeError
             else:
                concatenation += karg + " "

        res = function(*args, **kargs)
        concatenation += str(res)
        print(concatenation)
    return wrapper


if __name__ == "__main__":

    print("Definisco la funzione ciao decorata con @decora. La funzione ciao restituisce il risultato di 2 + 2")

    @decora
    def ciao(*args, **kargs):
        return 2 + 2

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 'stai'. Mi aspetto: 'ciao come stai? 4'")
    ciao("ciao", "come", "stai?")

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 3. Mi aspetto: Type Error")
    try:
        ciao("ciao", "come", 3)
    except TypeError:
        print("Type Error catturato")

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 'stai?' e "
          "parametro keyword key = 3. Mi aspetto: Type Error")
    try:
        ciao("ciao", "come", "stai?", key=3)
    except TypeError:
        print("Type Error catturato")

    print("chiamo la funzione ciao con parametri: 'ciao', 'come', 'stai?' e "
          "parametro keyword key = '3'. Mi aspetto: 'Ciao come stai? 3 4'")
    ciao("ciao", "come", "stai?", key = "3")


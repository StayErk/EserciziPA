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

@decora
def ciao(*args, **kargs):
    return 2 + 2



ciao("ciao", "come", "stai?", key=3)

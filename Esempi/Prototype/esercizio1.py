class AClass:
    __slots__ = ['nome', 'cognome', 'eta']
    def __init__(self, nome = None, cognome = None, eta = None):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

class Borg:
    _sharedState = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = Borg._sharedState
        return obj

def main():
    b = Borg()
    b.x1 = "ciao"
    b.x2 = "mortadella"

    c = Borg()

    print("b.x1", b.x1, "\nb.x2", b.x2)
    print("c.x1", c.x1, "\nc.x2", c.x2)

if __name__ == "__main__":
    main()

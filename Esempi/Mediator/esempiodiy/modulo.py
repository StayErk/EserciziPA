import collections

class Mediated:
    def __init__(self):
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)

class Incendio(Mediated):
    def __init__(self):
        super().__init__()
        self.fiamme = False

    def scoppia(self):
        self.fiamme = True
        self.on_change()

class VigileDF(Mediated):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.inServizio = False

    def impegnato(self):
        self.inServizio = True

    def disimpegna(self):
        self.inServizio = False

    def spegneIncendio(self):
        self.on_change()

class Mediator:
    def __init__(self, mediatedCallablePairs: list):
        self.callablesForMediated = collections.defaultdict(list)
        for membro, callable in mediatedCallablePairs:
            self.callablesForMediated[membro].append(callable)
            membro.mediator = self

    def on_change(self, mediated):
        callablesMembro = self.callablesForMediated[mediated]
        if callablesMembro is not None:
            for callable in callablesMembro:
                callable(mediated)

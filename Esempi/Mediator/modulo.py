import collections

class Mediated:
    def __init__(self) -> None:
        self.mediator = None

    def on_change(self) -> None:
        if self.mediator is not None:
            self.mediator.on_change(self)


class Cane(Mediated):

    def __init__(self, nome:str, ora) -> None:
        super().__init__()
        self.nome = nome

        #ora in cui il cane ha mangiato l'ultima volta
        self.oraUltimoPasto = ora

    def abbaia(self):
        self.on_change()


class Persona(Mediated):

    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome

        # se la persona è fuori casa questa variabile è settata a -1
        self.oraRitorno = 0

    def tornaACasa(self, ora):
        print("{} torna a casa alle ore {}".format(self.nome, ora.strftime('%H:%M')))
        self.on_change()

    def esce(self):
        print("{} esce di casa.".format(self.nome))
        self.oraRitorno = -1


class Mediator:
    def __init__(self, memberCallablePairs):
        self.callablesForMember = collections.defaultdict(list)
        for membro, caller in memberCallablePairs:
            self.callablesForMember[membro].append(caller)
            membro.mediator = self

    # member può essere un cane o una persona
    def on_change(self, member):
        callables = self.callablesForMember.get(member)
        if callables is not None:
            for caller in callables:
                caller(member)
        else:
            raise AttributeError("Nessun metodo registrato per {}".format(str(member)))

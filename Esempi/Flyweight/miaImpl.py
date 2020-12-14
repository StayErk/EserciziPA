class FW:

    def __init__(self, sharedState):
        self._sharedState = sharedState

    def op(self, itsOwnState: list, tipo: type, fileName: str):
        statoCondiviso = str(self._sharedState)
        statoProprio = str(itsOwnState)
        oggetto = tipo(self._sharedState + itsOwnState)
        output_file = open(fileName, 'a')
        output_file.write("FW: nuovo {}, con stato condiviso ({}) e stato proprio ({})".format(str(tipo), statoCondiviso, statoProprio))
        print("Il nuovo oggetto è di tipo {} con stato {}".format(tipo, str(oggetto.state)))

        output_file.close()
        return oggetto


class FW_factory:
    _FWDict = {}

    def __init__(self, initialFW: list):
        for state in initialFW:
            self._FWDict[self.get_key(state)] = FW(state)

    def get_key(self, state: list):
        return "_".join(sorted(state))

    def get_FW(self, sharedState: list)-> FW:
        key = self.get_key(sharedState)

        if not self._FWDict.get(key):
            print("Creo un nuovo FW")
            self._FWDict[key] = FW(sharedState)
        else:
            print("Uso un fw esistente")
    
        return self._FWDict[key]

    def list_FW(self):
        count = len(self._FWDict)
        print("FW_factory ho {} oggetti FW".format(count))
        print("\n".join(self._FWDict.keys()), end="")

class Car:
    def __init__(self, state: list):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

def add(factory: FW_factory, targa: str, proprietario: str, marca: str, modello: str, colore: str):
    print("\n\nAggiungo una macchina")
    fw = factory.get_FW([marca, modello, colore])
    fw.op([targa, proprietario], Car, "cars.txt")

if __name__ == "__main__":

    factory = FW_factory([["Chevrolet", "Camaro", "rosa"], ["Mercedes Benz", "Classe A", "nera"]])

    factory.list_FW()

    add(factory, "DE123AT", "Andrea Ercolino", "Chevrolet", "Camaro", "rosa")
    add(factory, "AB321CT", "Maria Chiara Nasto", "Mercedes Benz", "Classe A", "grigia")

    factory.list_FW()

class FW:
    def __init__(self, sharedState: list):
        self._shared_state = sharedState

    def op(self, ownState: list, tipo:type, file: str):
        s = str(self._shared_state)
        o = str(ownState)
        oggetto = tipo(self._shared_state + ownState)
        of = open(file, 'a')
        of.write("Inserisco {} nel file con stato condiviso {} e stato proprio {}".format(str(tipo), s, o))
        of.close()
        return oggetto

class FWFactory:
    _FWDict = {}

    def __init__(self, initialFW: list):
        for state in initialFW:
            self._FWDict[self.get_key(state)] = FW(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_FW(self, state) -> FW:
        key = self.get_key(state)

        if not self._FWDict.get(key):
            print("Creato FW non presente")
            self._FWDict[key] = FW(state)

        return self._FWDict[key]

    def list_fws(self):
        count = len(self._FWDict)
        print("\n".join(self._FWDict.keys()), end="")
        print("\n")

class PC:
    def __init__(self, state: list):
        self._state = state

    def state(self):
        return self._state

def add(factory: FWFactory, dimensioniCase: str, coloreCase: str, processore: str, gpu: str):
    fw = factory.get_FW([dimensioniCase, coloreCase])
    fw.op([processore, gpu], PC, "pc_da_assemblare.txt")

if __name__ == "__main__":
    factory = FWFactory([
        ["mid tower", "nero"],
        ["full tower", "nero"],
        ["full tower", "bianco"],
        ["full tower", "grigio"],
        ["mid tower", "grigio"]
    ])

    factory.list_fws()

    add(factory, "mid tower", "bianco", "i9-9900k", "rtx 2080Ti")
    add(factory, "full tower", "nero", "i7-7700k", "rtx 2070")

    factory.list_fws()


import modulo

class Caserma:
    def __init__(self, nomeVigile1: str, nomeVigile2: str):
        self.allerta = False
        self.vigile1 = modulo.VigileDF(nomeVigile1)
        self.vigile2 = modulo.VigileDF(nomeVigile2)
        self.incendio = modulo.Incendio()
        self.create_mediator()

    def create_mediator(self):
        self.mediator = modulo.Mediator(((self.vigile1, self.spegne_incendio), (self.vigile2, self.spegne_incendio), (self.incendio, self.allarmeIncendio), (self.vigile2, self.torna_caserma), (self.vigile1, self.torna_caserma)))

    def allarmeIncendio(self, incendio):
        if self.allerta == False:
            print("Scoppia Incendio")
            self.allerta = True

    def spegne_incendio(self, vigile: modulo.VigileDF):
        if self.allerta == True:
            if vigile.inServizio == False:
                vigile.impegnato()
                self.incendio.fiamme =False
                self.allerta = False
                print("Vigile {} spegne l'incendio, è impegnato a tornare: {}".format(vigile.nome, vigile.inServizio))
        else:
            print("Nessun Incendio in corso")

    def torna_caserma(self, vigile: modulo.VigileDF):
        if vigile.inServizio == True:
            print("Il vigile {} torna in caserma".format(vigile.nome))
            self.vigile1.disimpegna()


if __name__ == "__main__":
    caserma = Caserma("Arturo", "Peppe")
    caserma.incendio.scoppia()
    caserma.vigile1.spegneIncendio()
    caserma.incendio.scoppia()
    caserma.vigile1.spegneIncendio()
    print(caserma.allerta, caserma.incendio.fiamme)
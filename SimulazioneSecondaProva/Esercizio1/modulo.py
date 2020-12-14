from collections import  defaultdict
 

class Pacco:

    ORDINATO, SPEDITO, RICEVUTO = ("ordinato", "spedito", "ricevuto")

    def __init__(self):
        self.callbacksFoEvent = defaultdict(list)
        self.state = Pacco.ORDINATO

    @property
    def state(self):
        if self._prec == None: return Pacco.ORDINATO
        if self._prec != None  and self._succ != None: return Pacco.SPEDITO
        if self._succ == None: return Pacco.RICEVUTO

    @state.setter
    def state(self, state):
        if state == Pacco.ORDINATO:
            self._prec = None
            self._succ = Pacco.SPEDITO
            self._statoAttuale = "il pacco è stato ordinato ma non ancora spedito"
        elif state == Pacco.SPEDITO:
            self._prec = Pacco.ORDINATO
            self._succ = Pacco.RICEVUTO
            self._statoAttuale = "il pacco è stato spedito ma non consegnato"
        else:
            self._prec = Pacco.SPEDITO 
            self._succ =  None
            self._statoAttuale = "consegno il pacco al destinatario"

    def stampaStato(self):
        print(self._statoAttuale)

    def next(self):
        if self._succ is not None:
            self.state = self._succ
        else: print("il pacco è già stato consegnato")

    def prec(self):
        if self._prec is not None:
            self.state = self._prec



def main():
	print("\nCreo il pacco")
	pacco=Pacco()
	pacco.stampaStato()
	print("\nInoltro il pacco all'ufficio postale")
	pacco.next()
	pacco.stampaStato()
	print("\nConsegno il pacco al destinatario")
	pacco.next()
	pacco.stampaStato()
	print("\nProvo a passare ad uno stato successivo")
	pacco.next()
	pacco.stampaStato()

if __name__== "__main__":
	main()


"""Il  programma deve stampare:
Creo 
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non 

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""

from datetime import date
import copy

class Alimento:

    E="elevata"
    M="media"
    N="nessuna"

    
    
    MAXIMM=100
    MAXCONSUMO=30
        
    def __init__(self,  nome):
        self.nome = nome
        self._scorta = 0
        self._consumo = {}
        self.disponibilita = Alimento.N
    
    def aggiorna(self,nome,usata,data):
        try:
            usataOld, dataOld = self._consumo[nome]
            self._consumo[nome]= (usataOld + usata, data)
        except KeyError:
            self._consumo[nome]= (usata, data)
        

    @property
    def disponibilita(self):
        if self.usa != self._usa and self.fai_scorta == self._fai_scorta: return Alimento.N
        if self.usa == self._usa and self.fai_scorta == self._fai_scorta: return Alimento.M
        if self.usa == self.usa and self.fai_scorta != self._fai_scorta: return Alimento.E

    @disponibilita.setter
    def disponibilita(self, value):
        if value == Alimento.N:
            self.usa = lambda *args: None
            self.fai_scorta=  self._fai_scorta
        elif value == Alimento.M:
            self.usa= self._usa
            self.fai_scorta = self._fai_scorta
        elif value == Alimento.E:
            self.usa = self._usa
            self.fai_scorta= lambda *args: None

    @property
    def scorta(self):
        return self._scorta

    
    @scorta.setter
    def scorta(self, value):
        self._scorta = value

    def _usa(self,nomePietanza,q,data):
        if q>Alimento.MAXCONSUMO or q>self.scorta:
            print("Attenzione: non e` posssibile usare la quantita`  {}  dell'alimento {}".format(q,self.nome))
            return
        else:
            self.scorta=self.scorta-q
            self.aggiorna(nomePietanza,q,data)
            if self.scorta==0:
                self.disponibilita=Alimento.N
            if 0<self.scorta<Alimento.MAXIMM:
                self.disponibilita=Alimento.M



    def butta_scorte(self):
        self.scorta=0
        self.disponibilita=Alimento.N
        
        
            
            
            
          

    def _fai_scorta(self,n):
        if n<=0 or n+self.scorta>Alimento.MAXIMM:
            return
        self.scorta=self.scorta+n
        if 0<self.scorta<Alimento.MAXIMM:
            self.disponibilita=Alimento.M
        if self.scorta==Alimento.MAXIMM:
                self.disponibilita=Alimento.E

def main():

    a1= Alimento("pomodoro in scatola")
    print("Inizialmente la disponibilita` dell'alimento {} e` {}".format(a1.nome,a1.disponibilita))
    print("Riforniamo la  dispensa di {} chili di {}".format(Alimento.MAXIMM,a1.nome))
    a1.fai_scorta(Alimento.MAXIMM)
    print("La disponibilita` dell'alimento {} e` {} e si dispone di una scorta di {} chili".format(a1.nome,a1.disponibilita,a1.scorta))
    print("Il ristorante deve usare 2 chili di {} per cucinare la Parmigiana".format(a1.nome))
    a1.usa("Parmigiana",2,date(2020,1,2))
    print("Il ristorante deve usare 3 chili di {} per cucinare le lasagne".format(a1.nome))
    a1.usa("Lasagne",3,date(2020,1,2))
    print("Il ristorante deve usare 4 chili di {} per cucinare le pizze".format(a1.nome))
    a1.usa("Pizza",4,date(2020,1,2))
    print("Il ristorante deve usare 1 chilo di {} per cucinare la pasta al pomodoro".format(a1.nome))
    a1.usa("Pasta al pomodoro",1,date(2020,1,3))
    print("Il ristorante deve usare 4 chili di {} per cucinare la Parmigiana".format(a1.nome))
    a1.usa("Parmigiana",4,date(2020,1,3))
    print("Il ristorante deve usare 3 chili di {} per cucinare le pappardelle con i funghi".format(a1.nome))
    a1.usa("Pappardelle con i funghi",3,date(2020,1,3))
    print("Il ristorante deve usare 4 chili di {} per cucinare la pasta al pomodoro".format(a1.nome))
    a1.usa("Pasta al pomodoro", 4,date(2020,1,4))
    print("Il ristorante deve usare 2 chili di {} per cucinare le pappardelle con i funghi".format(a1.nome))
    a1.usa("Pappardelle con i funghi",2,date(2020,1,4))
    
     
    print("\nQueste sono le quantita` di {} usate dall'inizio del 2020  per ciascuna pietanza:".format(a1.nome))
    for k,v in a1._consumo.items():
        print("Fino al giorno {} sono stati usati {} chili di {} per cucinare la pietanza {}".format(v[1],v[0],a1.nome,k))
    print("Eliminiamo le scorte di {}".format(a1.nome))
    a1.butta_scorte()
    if a1.scorta==0:
        print("Non vi sono piu` scorte di  {} in magazzino".format(a1.nome))
    
    else:
        print("qualcosa non va nell'implementazione")
    
        
        

if __name__== "__main__":
	main()
    
        
        
       
"""Il programma deve stampare:

Inizialmente la disponibilita` dell'alimento pomodoro in scatola e` nessuna
Riforniamo la  dispensa di 100 chili di pomodoro in scatola
La disponibilita` dell'alimento pomodoro in scatola e` elevata e si dispone di una scorta di 100 chili
Il ristorante deve usare 2 chili di pomodoro in scatola per cucinare la Parmigiana
Il ristorante deve usare 3 chili di pomodoro in scatola per cucinare le lasagne
Il ristorante deve usare 4 chili di pomodoro in scatola per cucinare le pizze
Il ristorante deve usare 1 chilo di pomodoro in scatola per cucinare la pasta al pomodoro
Il ristorante deve usare 4 chili di pomodoro in scatola per cucinare la Parmigiana
Il ristorante deve usare 3 chili di pomodoro in scatola per cucinare le pappardelle con i funghi
Il ristorante deve usare 4 chili di pomodoro in scatola per cucinare la pasta al pomodoro
Il ristorante deve usare 2 chili di pomodoro in scatola per cucinare le pappardelle con i funghi

Queste sono le quantita` di pomodoro in scatola usate dall'inizio del 2020  per ciascuna pietanza:
Fino al giorno 2020-01-03 sono stati usati 6 chili di pomodoro in scatola per cucinare la pietanza Parmigiana
Fino al giorno 2020-01-02 sono stati usati 3 chili di pomodoro in scatola per cucinare la pietanza Lasagne
Fino al giorno 2020-01-02 sono stati usati 4 chili di pomodoro in scatola per cucinare la pietanza Pizza
Fino al giorno 2020-01-04 sono stati usati 5 chili di pomodoro in scatola per cucinare la pietanza Pasta al pomodoro
Fino al giorno 2020-01-04 sono stati usati 5 chili di pomodoro in scatola per cucinare la pietanza Pappardelle con i funghi
Eliminiamo le scorte di pomodoro in scatola
Non vi sono piu` scorte di  pomodoro in scatola in magazzino


"""


    
    
        
        
        
        






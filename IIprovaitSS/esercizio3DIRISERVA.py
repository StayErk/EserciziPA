#modulo che simula il comportamento di AlimentoOsservato
#puo` essere usato al posto di esercizio3.py da chi non ha completato il codice di esercizio2.py
#non usare questo modulo per risolvere l'esercizio 1 e\o l'esercizio 2 perche' il codice in questo modulo non
# soddisfa in alcun modo i requisiti richiesti da quei due esercizi.

#GUARDATE IL MAIN PER CAPIRE COSA PASSARE AD UPDATE. IN PARTICOLARE SI NOTI CHE LE STRINGHE DA PASSARE NEI 4 DIVERSI CASI SONO LE SEGUENTI:
# 'nuova_vendita','immagazzinata_nuova_quantita','modifica_stato_scorte'. 'nuovo_acquirente'

from datetime import date
import copy
import itertools
import random
import functools

class AlimentoOsservato:

    E="elevata"
    M="media"
    N="nessuna"
    
    
    MAXIMM=100
    MAXCONSUMO=30
        
    

    def __init__(self,  nome):
       
        self.nome=nome
        self.scorta=0
        self._observers=set()
        self.disponibilita=AlimentoOsservato.N
        
        
       
    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self._observers.add(observer)
            observer.update(self,None)

    

            
    def usa(self,nomePietanza,q,data):
        if q>AlimentoOsservato.MAXCONSUMO or q>self.scorta:
            print("Attenzione: non e` posssibile usare la quantita`  {}  dell'alimento {}".format(q,self.nome))
            return
        else:
            self.scorta=self.scorta-q
           
            if self.scorta==0:
                self.disponibilita=AlimentoOsservato.N
            if 0<self.scorta<AlimentoOsservato.MAXIMM:
                self.disponibilita=AlimentoOsservato.M


    

    def fai_scorta(self,n):
        if n<=0 or n+self.scorta>AlimentoOsservato.MAXIMM:
            return
        self.scorta=self.scorta+n
        if 0<self.scorta<AlimentoOsservato.MAXIMM:
            self.disponibilita=AlimentoOsservato.M
        if self.scorta==AlimentoOsservato.MAXIMM:
                self.disponibilita=AlimentoOsservato.E







            
class Ristorante:

    def __init__(self,nome:str,listaAlimenti:list):
        self.nome=nome
        self.alimenti=list()
        for a in listaAlimenti:
            self.alimenti.append(a)
        

    
    def update(self,s,alimento):
        self.handler = gestore_uso(gestore_nuova_scorta(gestore_cambioStato(gestore_np(gestoreDiDefault(None)))))
        self.delegate(s,alimento)

    #completare questo metodo che invia al gestore la richiesta e prima di uscire invoca ...
    def delegate(self, s, alimento):
     

    
        

def main():
    a1= AlimentoOsservato("pomodoro in scatola")
    a2= AlimentoOsservato("mozzarella")
    
    print("Inizialmente la disponibilita` dell'alimento {} e` {}".format(a1.nome,a1.disponibilita))
    print("Inizialmente la disponibilita` dell'alimento {} e` {} \n".format(a2.nome,a2.disponibilita))
    
    ristorante=Ristorante("RistoranteSalerno",[a1,a2])
   
    
    for a in ristorante.alimenti:
        a.observers_add(ristorante)
        a.fai_scorta(AlimentoOsservato.MAXIMM)
        ristorante.update('nuova_scorta',a)
        ristorante.update('cambio_stato',a)
        print()
    
    
    c=0
    for a in ristorante.alimenti:
        a.usa("Parminana",10+c,date(2020,10,1))
        ristorante.update('nuova_pietanza',a)
        ristorante.update('nuovo_uso',a)
        a.usa("Pizza",20+c,date(2020,10,1))
        ristorante.update('nuovo_uso',a)
        a.usa("Pasta al forno",5+c,date(2020,10,1))
        ristorante.update('nuovo_uso',a)
        a.usa("Parminana",3+c,date(2020,11,1))
        ristorante.update('nuovo_uso',a)
        if c==10: ristorante.update('modifica_stato_scorte',a)
        a.usa("Pasta al forno",4+c,date(2020,1,1))
        ristorante.update('nuovo_uso',a)
        c+=10

    
        

if __name__== "__main__":
    main()




"""Il programma deve stampare:


Inizialmente la disponibilita` dell'alimento pomodoro in scatola e` nessuna
Inizialmente la disponibilita` dell'alimento mozzarella e` nessuna 


Immagazzinata una nuova quantita` dell’alimento pomodoro in scatola: quantita` disponibile = 100
È cambiata la disponibilita` dell’alimento pomodoro in scatola: la disponibilita` ora è elevata 


Immagazzinata una nuova quantita` dell’alimento mozzarella: quantita` disponibile = 100
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è elevata 

Alimento pomodoro in scatola usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 90

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 70

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 65

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 62

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 58
Alimento mozzarella usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 80

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 50

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 35

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 22
Necessario fare scorta dell’alimento mozzarella


Nuovo uso dell’alimento mozzarella: quantita` disponibile = 86

"""

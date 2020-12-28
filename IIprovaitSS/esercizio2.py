from datetime import date
import copy
import itertools
import random



class AlimentoOsservato:

    E="elevata"
    M="media"
    N="nessuna"
    
    
    MAXIMM=100
    MAXCONSUMO=30
        
    

    def __init__(self,  nome):
        self.nome = nome
        self._observers = set()
        self._scorta = 0
        self._consumo = {}
        self.disponibilita = AlimentoOsservato.N
        
         

       
    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self._observers.add(observer)
            #Decidere voi cosa passare ad update (al posto dei puntini)
            observer.update(None)

    def observer_discard(self, observer): self._observers.discard(observer)

    #questo metodo deve notificaree un cambio stato agli ossservatori invocando il metodo update dell'osservatore
    def observers_notify(self, ob):
        for observer in self._observers:
            observer.update(ob)
        
    @property
    def disponibilita(self):
        if self.usa != self._usa and self.fai_scorta == self._fai_scorta: return AlimentoOsservato.N
        if self.usa == self._usa and self.fai_scorta == self._fai_scorta: return AlimentoOsservato.M
        if self.usa == self.usa and self.fai_scorta != self._fai_scorta: return AlimentoOsservato.E

    @disponibilita.setter
    def disponibilita(self, value):
        if value == AlimentoOsservato.N:
            self.usa = lambda *args: None
            self.fai_scorta=  self._fai_scorta
            self.observers_notify(["chdisp", self])
        elif value == AlimentoOsservato.M:
            self.usa= self._usa
            self.fai_scorta = self._fai_scorta
            self.observers_notify(["chdisp", self])
        elif value == AlimentoOsservato.E:
            self.usa = self._usa
            self.fai_scorta= lambda *args: None
            self.observers_notify(["chdisp", self])

    @property
    def scorta(self):
        return self._scorta

    
    @scorta.setter
    def scorta(self, value):
        oldScorta = self._scorta
        self._scorta = value
        if oldScorta < self._scorta:
            self.observers_notify(["immagazzinata", self])

    
    def aggiorna(self,nomeP,usata,data):
        self.observers_notify(["pietanza", self])
        try:
            usataOld, dataOld = self._consumo[nomeP]
            self._consumo[nomeP]= (usataOld + usata, data)
        except KeyError:
            self._consumo[nomeP]= (usata, data)
            self.observers_notify(["nuovap", self, data])   
        
    def _usa(self,nomePietanza,q,data):
        if q>AlimentoOsservato.MAXCONSUMO or q>self.scorta:
            print("Attenzione: non e` posssibile usare la quantita`  {}  dell'alimento {}".format(q,self.nome))
            return
        else:
            self.scorta=self.scorta-q
            self.aggiorna(nomePietanza,q,data)
            if self.scorta==0:
                self.disponibilita=AlimentoOsservato.N
            if 0<self.scorta<AlimentoOsservato.MAXIMM:
                self.disponibilita=AlimentoOsservato.M


    #serve per il test in esercizio1.py se usate questa classe anche nell'esercizio 1
    def butta_scorte(self):
        self.scorta=0
        self.disponibilita=AlimentoOsservato.N
        

    def _fai_scorta(self,n):
        if n<=0 or n+self.scorta>AlimentoOsservato.MAXIMM:
            return
        self.scorta=self.scorta+n
        if 0<self.scorta<AlimentoOsservato.MAXIMM:
            self.disponibilita=AlimentoOsservato.M
        if self.scorta==AlimentoOsservato.MAXIMM:
                self.disponibilita=AlimentoOsservato.E
                
              
             
    
    
       
#completare le due seguenti classi
class Ristorante:

    def __init__(self,nome:str,lista:list):
        self.nome=nome
        self.alimenti=list()
        for p in lista:
            self.alimenti.append(p)


    #metodo update: AGGIUNGETE VOI UNO O PIU` PARAMETRI AL POSTO DEI PUNTINI
    def update(self, ob):
        if ob == None: pass
        elif ob[0] == "pietanza":
            print("\nNuovo uso dell'alimento {}: quantità disponibie= {}".format(ob[1].nome, ob[1].scorta))
            if ob[1].scorta <  AlimentoOsservato.MAXIMM / 4:
                print("Necessario fare scorta dell'alimento: {}".format(ob[1].scorta))
                ob[1].fai_scorta(AlimentoOsservato.MAXIMM - ob[1].scorta)
        elif ob[0] == "immagazzinata":
            print("Immagazzinata nuova quantita dell'alimento {}: quantita  disponibile = {}".format(ob[1].nome, ob[1].scorta))
        elif ob[0] == "nuovap":
            print("Alimento {} usato per preparare una pietanza mai cucinata dall'inizio dell'anno".format(ob[1].nome))
        elif ob[0] == "chdisp":
            print("E' cambiata la disponibilita dell'alimento {}: la dsponibilita ora è: {}".format(ob[1].nome, ob[1].disponibilita))
            
class StoricoRistorante:
    def __init__(self):
        self.storico=[]
        
    #metodo update: AGGIUNGETE VOI UNO O PIU` PARAMETRI AL POSTO DEI PUNTINI
    def update(self, ob):
        if ob == None: pass
        elif ob[0] == "nuovap":
            stringa = "\nGiorno {}: l'alimento {} è stato usato per preparare una pietanza mai  cucinata da inizio anno".format(ob[2], ob[1].nome)
            self.storico.append(stringa)
        

    def stampa_report(self):
        o=open("Report.txt","a")
        for s in self.storico:
            o.write(s+"\n")
        o.close()
        
    
    

def main():
    a1= AlimentoOsservato("pomodoro in scatola")
    a2= AlimentoOsservato("mozzarella")
    
    print("Inizialmente la disponibilita` dell'alimento {} e` {}".format(a1.nome,a1.disponibilita))
    print("Inizialmente la disponibilita` dell'alimento {} e` {} \n".format(a2.nome,a2.disponibilita))
    
    ristorante=Ristorante("RistoranteSalerno",[a1,a2])
    storico_ristorante=StoricoRistorante()
    
    
    for a in ristorante.alimenti:
        a.observers_add(ristorante,storico_ristorante)
        a.fai_scorta(AlimentoOsservato.MAXIMM)
        print()
    
    
    c=0
    for a in ristorante.alimenti:
        a.usa("Parminana",10+c,date(2020,10,1))
        a.usa("Pizza",20+c,date(2020,10,1))
        a.usa("Pasta al forno",5+c,date(2020,10,1))
        a.usa("Parminana",3+c,date(2020,11,1))
        a.usa("Pasta al forno",4+c,date(2020,1,1))
        c+=10

    
    print("\n\nCreo un report")
    storico_ristorante.stampa_report()
        
   

if __name__== "__main__":
    main()
    
        
        
       
"""Il programma deve stampare:
Inizialmente la disponibilita` dell'alimento pomodoro in scatola e` nessuna
Inizialmente la disponibilita` dell'alimento mozzarella e` nessuna 

Immagazzinata una nuova quantita` dell’alimento pomodoro in scatola: quantita` disponibile = 100 chili
È cambiata la disponibilita` dell’alimento pomodoro in scatola: la disponibilita` ora è elevata

Immagazzinata una nuova quantita` dell’alimento mozzarella: quantita` disponibile = 100 chili
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è elevata


Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 90
Alimento pomodoro in scatola usato per cucinare una pietanza mai cucinata dall’inizio dell’anno
È cambiata la disponibilita` dell’alimento pomodoro in scatola: la disponibilita` ora è media

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 70
Alimento pomodoro in scatola usato per cucinare una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 65
Alimento pomodoro in scatola usato per cucinare una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 62

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 58

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 80
Alimento mozzarella usato per cucinare una pietanza mai cucinata dall’inizio dell’anno
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è media

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 50
Alimento mozzarella usato per cucinare una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 35
Alimento mozzarella usato per cucinare una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 22
Necessario fare scorta dell'alimento mozzarella
Immagazzinata una nuova quantita` dell’alimento mozzarella: quantita` disponibile = 100 chili
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è elevata

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 86
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è media


Creo un report
>>> 
"""



"""Il file Report contiene:


Giorno 2020-10-01 : l’alimento pomodoro in scatola è stato usato per cucinare una pietanza mai cucinata da inizio anno

Giorno 2020-10-01 : l’alimento pomodoro in scatola è stato usato per cucinare una pietanza mai cucinata da inizio anno

Giorno 2020-10-01 : l’alimento pomodoro in scatola è stato usato per cucinare una pietanza mai cucinata da inizio anno

Giorno 2020-10-01 : l’alimento mozzarella è stato usato per cucinare una pietanza mai cucinata da inizio anno

Giorno 2020-10-01 : l’alimento mozzarella è stato usato per cucinare una pietanza mai cucinata da inizio anno

Giorno 2020-10-01 : l’alimento mozzarella è stato usato per cucinare una pietanza mai cucinata da inizio anno
"""


    
    
        
        
        
        






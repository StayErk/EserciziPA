from esercizio2 import AlimentoOsservato


class Ristorante:

    def __init__(self,nome:str,listaAlimenti:list):
        self.nome=nome
        self.alimenti=list()
        for p in listaAlimenti:
            self.alimenti.append(p)
        

    
    def update(self,alimento, s):
        self.handler = gestore_uso(gestore_nuova_scorta(gestore_cambioStato(gestore_np(gestoreDiDefault(None)))))
        self.delegate(alimento,s[0],s[1])

    #completare questo metodo che invia al gestore la richiesta e prima di uscire invoca ...
    def delegate(self, s,alimento):
        
        







def main():
    a1= AlimentoOsservato("pomodoro in scatola")
    a2= AlimentoOsservato("mozzarella")
    
    print("Inizialmente la disponibilita` dell'alimento {} e` {}".format(a1.nome,a1.disponibilita))
    print("Inizialmente la disponibilita` dell'alimento {} e` {} \n".format(a2.nome,a2.disponibilita))
    
    ristorante=Ristorante("RistoranteSalerno",[a1,a2])
   
    
    for a in ristorante.alimenti:
        a.observers_add(ristorante)
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

    
        

if __name__== "__main__":
    main()
    
        
        



    
"""Il programma deve stampare:
Inizialmente la disponibilita` dell'alimento pomodoro in scatola e` nessuna
Inizialmente la disponibilita` dell'alimento mozzarella e` nessuna 


Immagazzinata una nuova quantita` dell’alimento pomodoro in scatola: quantita` disponibile = 100
È cambiata la disponibilita` dell’alimento pomodoro in scatola: la disponibilita` ora è elevata 


Immagazzinata una nuova quantita` dell’alimento mozzarella: quantita` disponibile = 100
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è elevata 


Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 90
Alimento pomodoro in scatola usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno
È cambiata la disponibilita` dell’alimento pomodoro in scatola: la disponibilita` ora è media 

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 70
Alimento pomodoro in scatola usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 65
Alimento pomodoro in scatola usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 62

Nuovo uso dell’alimento pomodoro in scatola: quantita` disponibile = 58

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 80
Alimento mozzarella usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è media 

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 50
Alimento mozzarella usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 35
Alimento mozzarella usato per cucinare  una pietanza mai cucinata dall’inizio dell’anno

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 22
Necessario fare scorta dell’alimento mozzarella
Immagazzinata una nuova quantita` dell’alimento mozzarella: quantita` disponibile = 100
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è elevata 

Nuovo uso dell’alimento mozzarella: quantita` disponibile = 86
È cambiata la disponibilita` dell’alimento mozzarella: la disponibilita` ora è media 

"""

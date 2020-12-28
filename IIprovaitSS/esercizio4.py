



from datetime import date

class AlimentoSemplice():
    
        
    def __init__(self,  nome):
        
        self.nome=nome
        
        self._consumo=dict()
        
       
    
    
    def aggiorna(self,nome,quantita,data):
        if self._consumo.get(nome)==None:
            self._consumo[nome]=(quantita,data)
        else:
            p=self._consumo[nome]
            self._consumo[nome]=(p[0]+quantita,data)
            




    
  


        
def main():
   
    a1= AlimentoSemplice("pomodoro in scatola")
    a2= AlimentoSemplice("mozzarella")
    a3= AlimentoSemplice("patate")
    a4=AlimentoSemplice("zucchero")
    a5=AlimentoSemplice("cioccolato")
    
    a1.aggiorna("Pizza",310,date(2019,10,30))
    a3.aggiorna("Patate fritte",300,date(2018,11,24))
    a1.aggiorna("Pasta al pomodoro",200,date(2019,6,11))
    a5.aggiorna("Torta al cioccolato",500,date(2016,2,10))
    a4.aggiorna("Torta al cioccolato",200,date(2016,2,10))
    alimenti=[a1,a2,a3,a4,a5]
    l1=[("Pizza",100,date.today())]
    s=25
    for c in range(ord('a'), ord('p')):
        l1.append(("Fantasia dello chef "+chr(c),s,date.today()))
        s+=10
    l2=[]
    s=30
    for c in range(ord('A'), ord('Y')):
        l2.append(("Fantasia dello chef "+chr(c),s,date.today()))
        s+=10
    l2.append(("Sorpresa dello chef",65,date.today()))
    

    l3=[]
    s=33
    for c in range(ord('A'), ord('W')):
        l3.append(("Sorpresa dello chef "+chr(c),s,date.today()))
        s+=10
    l4=[]
    s=11
    for c in range(ord('M'), ord('X')):
        l4.append(("Torta "+chr(c),s,date.today()))
        s+=10
    l5=[]
    s=39
    for c in range(ord('F'), ord('Q')):
        l5.append(("Torta "+chr(c),s,date.today()))
        s+=10
    l5.append(("Crema al cioccolato",20,date.today()))
    
    liste_acquirenti=[l1,l2,l3,l4,l5]
    processaAlimenti(alimenti,liste_acquirenti,3)

    
if __name__ == "__main__":
    main()

"""Il programma deve stampare (l'ordine in cui vengono stampate le informazioni relative a ciscun prodotto puo` cambiare):

Il dizionario _consumo  di pomodoro in scatola contiene 17 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
Pizza 410 2020-12-21
Pasta al pomodoro 200 2019-06-11
Fantasia dello chef a 25 2020-12-21
Fantasia dello chef b 35 2020-12-21
Fantasia dello chef c 45 2020-12-21
Fantasia dello chef d 55 2020-12-21
Fantasia dello chef e 65 2020-12-21
Fantasia dello chef f 75 2020-12-21
Fantasia dello chef g 85 2020-12-21
Fantasia dello chef h 95 2020-12-21
Fantasia dello chef i 105 2020-12-21
Fantasia dello chef j 115 2020-12-21
Fantasia dello chef k 125 2020-12-21
Fantasia dello chef l 135 2020-12-21
Fantasia dello chef m 145 2020-12-21
Fantasia dello chef n 155 2020-12-21
Fantasia dello chef o 165 2020-12-21

Il dizionario _consumo  di mozzarella contiene 25 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
Fantasia dello chef A 30 2020-12-21
Fantasia dello chef B 40 2020-12-21
Fantasia dello chef C 50 2020-12-21
Fantasia dello chef D 60 2020-12-21
Fantasia dello chef E 70 2020-12-21
Fantasia dello chef F 80 2020-12-21
Fantasia dello chef G 90 2020-12-21
Fantasia dello chef H 100 2020-12-21
Fantasia dello chef I 110 2020-12-21
Fantasia dello chef J 120 2020-12-21
Fantasia dello chef K 130 2020-12-21
Fantasia dello chef L 140 2020-12-21
Fantasia dello chef M 150 2020-12-21
Fantasia dello chef N 160 2020-12-21
Fantasia dello chef O 170 2020-12-21
Fantasia dello chef P 180 2020-12-21
Fantasia dello chef Q 190 2020-12-21
Fantasia dello chef R 200 2020-12-21
Fantasia dello chef S 210 2020-12-21
Fantasia dello chef T 220 2020-12-21
Fantasia dello chef U 230 2020-12-21
Fantasia dello chef V 240 2020-12-21
Fantasia dello chef W 250 2020-12-21
Fantasia dello chef X 260 2020-12-21
Sorpresa dello chef 65 2020-12-21

Il dizionario _consumo  di patate contiene 23 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
Patate fritte 300 2018-11-24
Sorpresa dello chef A 33 2020-12-21
Sorpresa dello chef B 43 2020-12-21
Sorpresa dello chef C 53 2020-12-21
Sorpresa dello chef D 63 2020-12-21
Sorpresa dello chef E 73 2020-12-21
Sorpresa dello chef F 83 2020-12-21
Sorpresa dello chef G 93 2020-12-21
Sorpresa dello chef H 103 2020-12-21
Sorpresa dello chef I 113 2020-12-21
Sorpresa dello chef J 123 2020-12-21
Sorpresa dello chef K 133 2020-12-21
Sorpresa dello chef L 143 2020-12-21
Sorpresa dello chef M 153 2020-12-21
Sorpresa dello chef N 163 2020-12-21
Sorpresa dello chef O 173 2020-12-21
Sorpresa dello chef P 183 2020-12-21
Sorpresa dello chef Q 193 2020-12-21
Sorpresa dello chef R 203 2020-12-21
Sorpresa dello chef S 213 2020-12-21
Sorpresa dello chef T 223 2020-12-21
Sorpresa dello chef U 233 2020-12-21
Sorpresa dello chef V 243 2020-12-21

Il dizionario _consumo  di zucchero contiene 12 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
Torta al cioccolato 200 2016-02-10
Torta M 11 2020-12-21
Torta N 21 2020-12-21
Torta O 31 2020-12-21
Torta P 41 2020-12-21
Torta Q 51 2020-12-21
Torta R 61 2020-12-21
Torta S 71 2020-12-21
Torta T 81 2020-12-21
Torta U 91 2020-12-21
Torta V 101 2020-12-21
Torta W 111 2020-12-21

Il dizionario _consumo  di cioccolato contiene 13 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
Torta al cioccolato 500 2016-02-10
Torta F 39 2020-12-21
Torta G 49 2020-12-21
Torta H 59 2020-12-21
Torta I 69 2020-12-21
Torta J 79 2020-12-21
Torta K 89 2020-12-21
Torta L 99 2020-12-21
Torta M 109 2020-12-21
Torta N 119 2020-12-21
Torta O 129 2020-12-21
Torta P 139 2020-12-21
Crema al cioccolato 20 2020-12-21

"""

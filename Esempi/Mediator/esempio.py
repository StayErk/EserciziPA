#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Esempio fornitoci a lezione dalla professoressa.

Si considerino le classi Cane e Persone fornite nel file modulo.py. Scrivere la classe Casa con due cani e una persona. La classe Casa fa uso di un mediatore per fare in modo che:
    * Quando almeno uno dei due cani abbaia allora viene settato a true un flag di allerta
    * Quando il padrone torna a casa,se il flag di allerta è true verifica per ciascun cane se tra
      l'ora in cui è tornato a casa e l'ora in cui il cane ha mangiato per l'ultima volta sono
      passate più di quattro ore. In questo caso da mangiare al cane.

      (ora1-ora2).total_seconds()/60/60 => differenza tra ore
"""
from datetime import datetime

from modulo import Mediator
from modulo import Cane
from modulo import Persona

class Casa:

    def __init__(self, nomePadrone: str, nomeCane1: str, nomeCane2: str, oraUltimaPappa1: datetime, oraUltimaPappa2: datetime) -> None:

        self.allerta = False
        self.padrone = Persona(nomePadrone)

        self.cane1 = Cane(nomeCane1, oraUltimaPappa1)
        self.cane2 = Cane(nomeCane2, oraUltimaPappa2)

        self.create_mediator()

    def create_mediator(self):

        self.mediator = Mediator(((self.padrone, self.da_pappa), (self.cane1, self.allerta_padrone), (self.cane2, self.allerta_padrone)))

    def allerta_padrone(self, cane: Cane):
        print("Il cane {} abbaia".format(cane.nome))
        if self.padrone.oraRitorno == -1:
            self.allerta = True

    def da_pappa(self, padrone: Persona):

        if self.allerta == True:
            if (self.padrone.oraRitorno - self.cane1.oraUltimoPasto).total_seconds()/60/60 > 4:
                print("{} da la pappa a {}".format(self.padrone.nome, self.cane1.nome))
                self.cane1.oraUltimoPasto = self.padrone.oraRitorno
            if (self.padrone.oraRitorno - self.cane2.oraUltimoPasto).total_seconds()/60/60 > 4:
                print("{} da la pappa a {}".format(self.padrone.nome, self.cane2.nome))

            self.allerta = False

def main():
    casa = Casa("Maria", "pippo", "pluto", datetime(year=2020, month=1, day=11, hour=10), datetime(year=2020, month=1, day=11, hour=11))

    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.tornaACasa(datetime(year=2020, month=1, day=11, hour=15))
    casa.padrone.esce()

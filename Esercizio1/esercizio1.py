#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Esercizio tratto dalla prima prova in itinere.
"""


def copyUpTo(L: 'lista',
             x: 'elemento da cercare') -> 'copia della lista che contiene gli elementi fino a x':
    if L == []:
        return []

    if L[0] == x:
        return []

    if L[0] != x:
        # accoda il risultato della chiamata ricorsiva copyUpTo
        # al primo elemento della lista L
        return L[:1]+copyUpTo(L[1:], x)

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    daCercare = 4
    print('Chiamo la funzione copyUpTo con l=', lista,
          'e x= ', daCercare, '\nMi aspetto: [1, 2, 3]')
    print(copyUpTo(lista, daCercare))


    daCercare = 6
    print('Chiamo la funzione copyUpTo con l=', lista,
        'e x= ', daCercare, '\nMi aspetto: [1, 2, 3, 4, 5]')
    print(copyUpTo(lista, daCercare))


    lista = []
    print('Chiamo la funzione copyUpTo con l=', lista,
          'e x= ', daCercare, '\nMi aspetto: []')
    print(copyUpTo(lista, daCercare))

    lista = ['a', 'b', 2.5, 4]
    daCercare = 2.5
    print('Chiamo la funzione copyUpTo con l=', lista,
          'e x= ', daCercare, '\nMi aspetto: [a, b]')
    print(copyUpTo(lista, daCercare))



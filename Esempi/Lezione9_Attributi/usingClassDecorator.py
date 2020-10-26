#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Questo esempio più complesso utilizza una decorator factory.
Ensure infatti è una funzione che restituisce un decoratore.
Il decoratore prodotto viene applicato alla classe 🤯
"""
import numbers
import re
# Funzioni di validazione

# la funzione is_in_range è una factory function che crea una nuova funzione
# is in range che ha i valori minimo e massimo codificati al suo interno


def is_in_range(minimum=None, maximum=None):
    # lancia AssertionError se una delle due condizioni è vera
    assert minimum is not None or maximum is not None

    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} deve essere un numero".format(name))
        if minimum is not None and value < minimum:
            raise ValueError("{} {} is to small".format(name, value))
        if maximum is not None and value > maximum:
            raise ValueError("{} {} is to big".format(name, value))
    return is_in_range


def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} deve essere una stringa".format(name))
    if not bool(value):
        raise ValueError("{} non deve essere una stringa vuota".format(name))



# regex bella complessa
def is_valid_isbn(name, value):
    regex = re.compile(
        r"^(?:ISBN(?:-1[03])?:? )?(?=[-0-9]{17}$|"
        r"[-0-9X ]{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?"
        r"(?:[0-9]+[- ]?){2}[0-9X]$")
    if regex.match(value):
        # logica di controllo dei codici ISBN
        digits = list(re.sub("[^0-9X]", "", value))
        checkSumDigit = digits.pop()
        if len(digits) == 9:
            checkValue = sum((x + 2) * int(y) for x, y in enumerate(
                reversed(digits)))
            check = 11 - (checkValue % 11)
            if check == 10:
                check = 'X'
            elif check == 11:
                check = "0"
        else:
            checkValue = sum((x % 2 * 2 + 1) * int(y) for x, y in enumerate(
                digits))

            check = 10 - (checkValue % 10)
            if check == 10:
                check = "0"

        if str(check) != checkSumDigit:
            raise ValueError(" non è isbn valido")
        return

    raise ValueError("non è isbn valido")


# Decorator factory
def ensure(name, validate, doc=None):
    def decorator(Class):
        privateName = "__" + name

        def getter(self):
            # privateName è una str che rappresenta il nome di un attributo
            return getattr(self, privateName)

        def setter(self, value):
            validate(name, value)
            setattr(self, privateName, value)
        setattr(Class, name, property(getter, setter, doc=doc))
        return Class
    return decorator


@ensure("title", is_non_empty_str)
@ensure("isbn", is_valid_isbn)
@ensure("price", is_in_range(1, 1000))
@ensure("quantity", is_in_range(0, 10000))
class Book:

    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity


b1 = Book("Programmazione avanzata", "ISBN 0321635906", 54.99, 7830)
print(b1)
b2 = Book("C++ e interfacce grafiche in Qt", "0132354160", 69.99, 15872)



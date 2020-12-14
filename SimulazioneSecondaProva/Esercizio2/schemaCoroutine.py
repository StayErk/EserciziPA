#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""
from functools import wraps

def coroutine(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        generatore = function(*args, **kwargs)
        next(generatore)
        return generatore
    return wrapper

@coroutine
def handlerOne(successor = None):
    while True:
        event = yield
        if 1 <= event <= 10:
            print ("HandlerOne ha gestito la richiesta '{}'".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def handlerTwo(successor = None):
    while True:
        event = yield
        if 11 <= event <= 20:
            print("HandlerTwo ha gestito la richiesta '{}'".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def handlerThree(successor = None):
    while True:
        event = yield
        if 21 <= event <= 30:
            print("HandlerThree ha gestito la richiesta '{}'".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def defaultHandler(successor = None):
    while True:
        event = yield
        if event < 1 or event > 30:
            print("DefaultHandler ha gestito la richiesta '{}'".format(event))
        elif successor is not None:
            successor.send(None)




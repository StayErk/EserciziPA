#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Implementazione esemplificativa MVC.
"""
import sys
import time
import datetime
import itertools

import random


# Classe base per tutte gli ogetti osservabili
class Observed:

    def __init__(self):
        self.__observers = set()

    def observer_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observer_notify(self):
        for observer in self.__observers:
            observer.update(self)

# Model
class SliderModel(Observed):

    def __init__(self, minimum, value, maximum):
        super().__init__();

        # ci assicuriamo che le proprietà esistano prima di usare il setter
        self.__minimum = self.__value = self.__maximum = None
        self.minimum = minimum
        self.value = value
        self.maximum = maximum

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.__value != value:
            self.__value = value
            self.observer_notify()
    @property
    def minimum(self):
        return self.__minimum
    
    @minimum.setter
    def minimum(self, value):
        self.__minimum = value
        self.observer_notify()

    @property
    def maximum(self):
        return self.__maximum
    
    @maximum.setter
    def maximum(self, value):
        self.__maximum = value
        self.observer_notify()


# primo osservatore
class HistoryView:
    
    def __init__(self):
        self.data = []

    def update(self, model: SliderModel):
        self.data.append((model.value, time.time()))

# secondo osservatore
class LiveView:

    def __init__(self, length = 40):
        self.length = length

    def update(self, model: SliderModel):
        tippingPoint = round(model.value * self.length / (model.maximum - model.minimum))

        td = '<td style="background-color: {}">&nbsp;</td>'
        html = ['<table style="font-family: monospace" border="0"><tr>']
        html.extend(td.format("darkblue") * tippingPoint)
        html.extend(td.format("cyan") * (self.length - tippingPoint))
        html.append("<td>{}</td></tr></table>".format(model.value))
        print("".join(html))

def main():
    historyView = HistoryView()
    liveView = LiveView()

    model = SliderModel(0, 0, 48)
    model.observer_add(historyView, liveView)

    for i in range(20):
        value = random.randint(0, 48)
        model.value = value

    for value, timestamp in historyView.data:
       print("{:3} {}".format(value, datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)

if __name__ == "__main__":
    main()

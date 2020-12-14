#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Questa implementazione dell'adapter utilizza un dizionario di metodi
"""

class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

class Robot:
    def __init__(self):
        self._execute = "I'm a robot"

    def execute(self):
        return str(self._execute)

    def __str__(self):
        return "Robot instace"

class Human:
    def __init__(self):
        self._say = "I'm a Human"

    def say(self):
        return str(self._say)

    def __str__(self):
        return "Human instance"


if __name__ == "__main__":
    objects = [Robot()]
    human = Human();

    objects.append(Adapter(human, dict(execute=human.say)))
    objects[0].execute()
    for i in objects:
        print("{}: {}".format(str(i), i.execute()))

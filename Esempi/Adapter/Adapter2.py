#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
In questo adapter si usa l'ereditarietà per svolgere tale funzione
"""

class Human:
    def say(self):
        return "Hello from Human!"

class Robot:
    def execute(self):
        return "I'm a ROBOT"

class Alien:
    def alienize(self):
        return "DESTROYING HUMANS!"

class Adapter(Robot):
    def __init__(self, whatIUse):
        self.whatIUse = whatIUse

    def execute(self):
        if isinstance(self.whatIUse, Human):
            return self.whatIUse.say()
        if isinstance(self.whatIUse, Alien):
            return self.whatIUse.alienize()
        else: return self.whatIUse.execute()

class WhatIUse:
    def op(self, comp):
        return comp.execute()

if __name__ == "__main__":
    whatIUse = WhatIUse()
    human = Human()
    alien = Alien()
    robot = Robot()

    adapt = Adapter(human)

    print(whatIUse.op(robot))
    print(whatIUse.op(adapt))
    adapt = Adapter(alien)
    print(whatIUse.op(adapt))

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



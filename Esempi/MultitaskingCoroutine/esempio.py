#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Implementazione dell'esercizio visto a lezione
"""
from functools import wraps
import re
import sys

flags = re.MULTILINE | re.IGNORECASE | re.DOTALL
URL_RE = re.compile(r"""href=(?P<quote>['"])(?P<url>[^\1]+?)""" r"""(?P=quote)""", re.IGNORECASE)
H1_RE = re.compile(r"<h1>(?P<h1>.+?)</h1>", flags)
H2_RE = re.compile(r"<h2>(?P<h2>.+?)</h2>", flags)




def coroutine(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        generatore = function(*args, **kwargs)
        next(generatore)
        return generatore
    return wrapper



@coroutine
def regex_matcher(receiver, regex):
    while True:
        testo_da_analizzare = yield
        for match in regex.finditer(testo_da_analizzare):
            receiver.send(match)
@coroutine
def reporter():
    ignore =frozenset({"style.css", "favicon.png", "index.html"})
    while True:
        match = yield
        if match is not None:
            groups = match.groupdict()
            if "url" in groups and groups["url"] not in ignore:
                print("\tURL:", groups["url"])
            elif "h1" in groups and groups["h1"] not in ignore:
                print("\tH1:", groups["h1"])
            elif "h2" in groups and groups["h2"] not in ignore:
                print("\tH2:", groups["h2"])

def main():
    print(sys.argv[1:])
    receiver = reporter()
    matchers = (regex_matcher(receiver, URL_RE), regex_matcher(receiver, H1_RE), regex_matcher(receiver, H2_RE))
    try:
        for fileName in sys.argv[1:]:
            print(fileName)
            html_input = open(fileName, encoding="utf-8").read()
            for matcher in matchers:
                matcher.send(html_input)
    finally:
        for matcher in matchers:
            matcher.close()
        receiver.close()



if __name__ == "__main__":
    main()

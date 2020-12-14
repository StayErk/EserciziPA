#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""
Esempio nel libro nel quale si fa una classe archivio che funge da facade 
per le classi gzip, tarfile e zipfile
"""

import zipfile
import re
import os
import gzip
import tarfile
import string
import sys
class Archive:

    def __init__(self, filename):
        # callable che restituisce una lista dei nomi dell'archivio
        self._names = None
        # mantiene un callable che estrae tutti i file dell'archivio
        self._unpack = None
        # file object aperto per accedere all'archivio
        self._file = None
        # mantiene il nome del file archivio
        self.filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, name):
        self.close()
        self.__filename = name

    def close(self):
        if self._file is not None:
            self._file.close()
        self._names = self._unpack = self._file = None

    def names(self):
        if self._file is None:
            self._prepare()
        return self._names()

    def unpack(self):
        if self._file is None:
            self._prepare()
            self._unpack()

    def _prepare(self):
        if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".zip")):
            self._prepare_tarball_or_zip()
        elif self.filename.endswith(".gz"):
            self._prepare_gzip()
        else:
            raise ValueError("unreadable: {}".format(self.filename))

    def is_safe(self, filename):
        return not (filename.startswith(("/", "\\")) or
    (len(filename) > 1 and filename[1] == ":" and filename[0].isalpha()) or
    re.search(r"[.][.][/\\]", filename))

    def _prepare_gzip(self):
        self._file = gzip.open(self.filename)
        filename = self.filename[:-3]
        self._names = lambda: [filename]
        def extractall():
            with open(filename, "wb") as file:
                file.write(self._file.read())
        self._unpack = extractall

    def _prepare_tarball_or_zip(self):
        def safe_extractall():
            unsafe = []
            for name in self.names():
                if not self.is_safe(name):
                    unsafe.append(name)
            if unsafe:
                raise ValueError("unsafe to unpack: {}".format(unsafe))
            self._file.extractall()
        if self.filename.endswith(".zip"):
            self._file = zipfile.ZipFile(self.filename)
            self._names = self._file.namelist
            self._unpack = safe_extractall
        else:
            suffix = os.path.splitext(self.filename)[1]
            self._file = tarfile.open(self.filename, 'r:'+ suffix[1:])
            self._names = self._file.getnames
            self._unpack = safe_extractall


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            sys.argv.index('-v')
            if sys.argv[1] == '-v':
                filename = sys.argv[2]
            else:
                filename = sys.argv[1]
            facade = Archive(filename)
            for x in facade.names():
                print(x)
            facade.unpack()
        except ValueError:
            print("uncorrect argument")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        facade = Archive(filename)
        facade.unpack()

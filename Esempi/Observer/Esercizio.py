"""
Classe LaureaT_Student che può essere osservata e che ha i seguenti attributi:
    total_cfu
    english_r se ha superato o no la prova di inglese
    grades: dizionario di esami sostenuti con elementi chiave nomeEsame e valore uguale a voto
    exam: tupla del tipo Exam che è una named tuple

Gli osservatori sono HystoryView e LiveView:
    HistoryView mantiene una lista di triple della forma dizionari esami superati, booleano se inglese superato, dat cambio di stato. Ogni tripla realizzata quando lo studente cambia stato

    LiveView esegue delle stante diverse al tipo di superamento

    link esempio macchine: fw.py
"""
from collections import namedtuple
import datetime
import itertools
import time
import sys
import copy



Exam = namedtuple("Exam", "name cfu")

class Observed:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer, ), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)

class HistoryView:

    def __init__(self):
        self.data = []

    def update(self, student):
        if student.english_r != None:
            self.data.append((copy.copy(student.grades), student.english_r, time.time()))
        else:
            self.data.append((copy.copy(student.grades), time.time()))

class LiveView:
    
    def __init__(self):
        self.__oldstate = None

    def update(self, student):
        if self.__oldstate == None:
            pass
        elif self.__oldstate.english_r != student.english_r:
            print("Cambio stato: lo studente ha appena superato la prova di inglese\n")
        elif self.__oldstate.grades != student.grades:
            print("Cambio stato: lo studente ha superato un nuovo esame")
            print("Cambio stato: il numero di CFU e': {}".format(student.total_cfu))
        self.__oldstate = copy.deepcopy(student)

class LaureaT_Student(Observed):
    
    def __init__(self, total_cfu, english_r = False, grade_dict=None):
        super().__init__()
        self.__total_cfu = self.__english_r = None
        
        self.total_cfu = total_cfu
        self.english_r = english_r

        if grade_dict != None:
            self.grades = grade_dict
        else: self.grades = {}

    @property
    def english_r(self):
        return self.__english_r

    @english_r.setter
    def english_r(self, value):
        if self.__english_r != value:
            self.__english_r = value
            self.observers_notify()

    @property
    def total_cfu(self):
        return self.__total_cfu

    @total_cfu.setter
    def total_cfu(self, value):
        if self.__total_cfu != value:
           self.__total_cfu = value
           self.observers_notify()

    def add_grade(self, exam, grade):
        if self.grades.get(exam.name) == None:
            self.grades[exam.name] = grade
            self.total_cfu = exam.cfu
            self.observers_notify()


def main():
    historyView =  HistoryView()
    liveView = LiveView()
    student = LaureaT_Student(0)
    student.observers_add(historyView, liveView)
    print("Lo studente sta per sostenere l'esame di analisi matematica")
    student.add_grade(Exam("Analisi Matematica", 9), 28)
    print("Lo studente sta per sostenere Sistemi Operativi")
    student.add_grade(Exam("Sistemi Operativi", 6), 20)
    print("Lo studente sta per sostenere l'esame di inglese")
    student.english_r = True

    for grades, flag, timestamp in historyView.data:
        print("Esami: {}, Inglese: {}, Data: {}".format(grades, "" if flag is None else "superato" if flag else "non superato", datetime.datetime.fromtimestamp(timestamp)))


if __name__ == "__main__":
    main()

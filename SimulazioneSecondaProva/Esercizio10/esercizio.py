"""
Esercizio 5 delle slide esercizidicembre2020
"""

class MyListCM:
    def __init__(self, lista):
        self.lista = lista

    def __enter__(self):
        return self.lista

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lista = None
        return True

if __name__ == "__main__":
    with MyListCM(["ciao", "come", "state"]) as list:
        for a in list:
            print(a)
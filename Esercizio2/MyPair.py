class MyPair:
    def __init__(self, key, value):
        self.key= key
        self.value= value

    def getValue(self):
        return self.value

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def setValue(self,  newValue):
        self.value= newValue

    def __eq__(self, myPair):
        return self.key == myPair.getKey() and self.value == myPair.getValue()

    def __ne__(self, myPair):
        return self.key != myPair.getKey() or self.value != myPair.getValue()

    def __str__(self):
        toReturn= '('
        toReturn += str(self.key)
        toReturn += ', '
        toReturn += str(self.value)
        toReturn += ')'
        return toReturn

if __name__ == '__main__':
    print("Inizializzo myPair con key= 1 e value= 'a'")
    x = MyPair(1, 'a')
    print("x=", x, end="\n\n")

    print("Stampo la chiave associata al valore 1: ")
    print ("x.getValue(1)=",  x.getValue(), end="\n\n")

    print("Stampo il valore associato alla chiave a: ")
    print ("x.getKey('a')=", x.getKey(), end="\n\n")

    print("Setto la key di x=2")
    x.setKey(2)
    print ("x.getKey())=", x.getKey(), "aspettato 2", end="\n\n")

    print("Setto il value di x='b'")
    x.setValue('b')
    print ("x.getValue()=", x.getValue(), "aspettato b", end="\n\n")

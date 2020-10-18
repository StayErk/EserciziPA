class Spam:
    numInstances = 0 # Cont le instanze della classe Spam
    def count(cls):
        cls.numInstances += 1

    def __init__(self):
        self.count()

    count = classmethod(count) # Lo rende un metodo di classe

class Sub(Spam):
    numInstances = 0 # Conta le instanze della classe Sub
    
    def __init__(self):
        Spam.__init__(self)

class Other(Sub): 
    numInstances = 0 # Conta le instanze della classe Other

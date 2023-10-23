from abc import ABC, abstractmethod

class AbstractDjur(ABC):  # En abstrakt klass

    @abstractmethod
    def tala(self):
        ...
    
    @abstractmethod
    def walk(self):
        pass

class Hund(AbstractDjur):

    def tala(self):
        return "Voff"

class Katt(AbstractDjur):

    def tala(self):
        return "Mjau"

class Ko(AbstractDjur):

    def tala(self):
        return "Råma"

min_ko = Ko()
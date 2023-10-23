from abc import ABC, abstractmethod

class JagTala(ABC):  # Detta fungerar som ett gränssnitt

    @abstractmethod
    def tala(self):
        pass

class Fisk(JagTala):

    def tala(self):
        return "Blub blub"

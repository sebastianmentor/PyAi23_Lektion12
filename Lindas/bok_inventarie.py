from bok import Bok

class Bokhandel:
    def __init__(self, namn) -> None:
        self.namn = namn
        self._lista_med_böcker:list[Bok] = []


    def söka_efter_bok(self, titel:str):
        for bok in self._lista_med_böcker:
            if titel == bok.get_title():  
                print(bok)

    def skriv_ut_alla_böcker(self):
        for bok in self._lista_med_böcker:
            print(bok)

    def lägg_till_ny_bok(self, titel, författare, pris, antal=None):
        if antal:
            ny_bok = Bok(titel,författare,pris, antal)
        else:
            ny_bok = Bok(titel, författare,pris)

        self._lista_med_böcker.append(ny_bok)

    def försäljning(self, titel, antal):
        pass
class Bok:
    def __init__(self, titel, författare, pris,antal=0) -> None:

        if not self.kontrollera_att_är_större_än_noll(pris):
            raise ValueError('Vi kan inte ha negativt pris!')

        self._titel = titel
        self._författare = författare
        self._pris = pris
        self._antal = antal

    def kontrollera_att_är_större_än_noll(self,pris) -> bool:
        return pris > 0
    
    def get_title(self) ->str:
        return self._titel
    
    def försäljning(self, antal_sålda):
        if antal_sålda > self._antal:
            print('Inte tillräckligt med böcker')
        else:
            self._antal -= antal_sålda
            if self._antal == 0:
                print('Skickar email om att varan är slut!')

    def __str__(self) -> str:
        return f'Titel:{self._titel:<20} Författare:{self._författare:<20} Pris:{self._pris:<10} Antal:{self._antal}'
    

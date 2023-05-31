import random

from Organizm import Organizm
from Organizm import Punkt


class Roslina(Organizm):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._inicjatywa = 0


    def akcja(self):
        self._wiek +=1
        self._nowy_organizm = False
        random_choice = random.randint(0, 40)
        if random_choice == 0:
            self.rozmnoz()
            return

    def kolizja(self, organizmAtakowany):
        if organizmAtakowany._sila > self._sila:
            self.umrzyj()
        else:
            organizmAtakowany.umrzyj()



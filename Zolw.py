from Zwierze import Zwierze
import random

class Zolw(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 2
        self._inicjatywa = 1
        self._nazwa = "Zolw"

    def stworzDziecko(self, x, y):
        zolw = Zolw(self._swiat, x, y)
        zolw._nowy_organizm = True
        return zolw

    def rysowanie(self):
        return (72, 99, 73)

    def czyOdpartoAtak(self, predator):
        return predator._sila < 5

    def akcja(self):
        random_choice = random.randint(0, 4)
        if random_choice == 0:
            super().akcja()
            return
        else:
            self._swiat._aplikacjaLogi.append(f'Zolw {self._polozenie.x, self._polozenie.y} nie wykonal ruchu w tej turze')
from Organizm import Organizm


class Zwierze(Organizm):
    _zasieg = 1

    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)

    def znajdzPustePole(self):
        x_docelowy = self._polozenie.x
        y_docelowy = self._polozenie.y
        


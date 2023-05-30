from Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 9
        self._inicjatywa = 5
        self._nazwa = "Wilk"

    def stworzDziecko(self, x, y):
        wilk = Wilk(self._swiat, x, y)
        wilk._nowy_organizm = True
        return wilk

    def rysowanie(self):
        return (89, 83, 82)
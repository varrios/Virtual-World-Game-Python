from Roslina import Roslina


class Trawa(Roslina):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 0
        self._nazwa = "Trawa"

    def stworzDziecko(self, x, y):
        trawa = Trawa(self._swiat, x, y)
        trawa._nowy_organizm = True
        return trawa

    def rysowanie(self):
        return (50, 252, 0)

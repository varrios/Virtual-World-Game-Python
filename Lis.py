from Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 3
        self._inicjatywa = 7
        self._nazwa = "Lis"

    def stworzDziecko(self, x, y):
        lis = Lis(self._swiat, x, y)
        lis._nowy_organizm = True
        return lis

    def rysowanie(self):
        return (255, 179, 0)

    def czyMaDobryWech(self):
        return True
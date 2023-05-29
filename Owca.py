from Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 4
        self._inicjatywa = 4
        self._nazwa = "Owca"

    def stworzDziecko(self, x, y):
        return Owca(self._swiat, x, y)

    def rysowanie(self):
        return (255, 255, 255)
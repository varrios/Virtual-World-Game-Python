from Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 99
        self._nazwa = "Wilcze Jagody"

    def stworzDziecko(self, x, y):
        wilczejagody = WilczeJagody(self._swiat, x, y)
        wilczejagody._nowy_organizm = True
        return wilczejagody

    def rysowanie(self):
        return (163, 51, 62)

    def czyTrujacy(self):
        return True

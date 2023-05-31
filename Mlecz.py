from Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 0
        self._nazwa = "Mlecz"

    def stworzDziecko(self, x, y):
        mlecz = Mlecz(self._swiat, x, y)
        mlecz._nowy_organizm = True
        return mlecz

    def rysowanie(self):
        return (233, 245, 5)

    def akcja(self):
        for i in range(3):
            super().akcja()

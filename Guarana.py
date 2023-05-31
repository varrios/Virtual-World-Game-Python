from Roslina import Roslina

class Guarana(Roslina):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 0
        self._nazwa = "Guarana"

    def stworzDziecko(self, x, y):
        guarana = Guarana(self._swiat, x, y)
        guarana._nowy_organizm = True
        return guarana

    def rysowanie(self):
        return (250, 2, 238)

    def dodajeSile(self, predator):
        predator._sila+=3
        return True
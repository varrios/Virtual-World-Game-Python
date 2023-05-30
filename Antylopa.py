from Zwierze import Zwierze
import random

class Antylopa(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 4
        self._inicjatywa = 4
        self._zasieg = 2
        self._nazwa = "Antylopa"

    def stworzDziecko(self, x, y):
        antylopa = Antylopa(self._swiat, x, y)
        antylopa._nowy_organizm = True
        return antylopa

    def rysowanie(self):
        return (252, 186, 3)

    def czyUcieczka(self, predator):
        random_choice = random.randint(0, 1)
        print(random_choice)
        if random_choice == 0:
            nowe_polozenie = predator.losujKierunekNiezajety()
            if nowe_polozenie.x == -1 or nowe_polozenie.y == -1:
                nowe_polozenie.x = self._polozenie.x
                nowe_polozenie.y = self._polozenie.y
            self.wykonajRuch(nowe_polozenie.x, nowe_polozenie.y)
            return True
        return False
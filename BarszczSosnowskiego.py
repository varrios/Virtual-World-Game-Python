from Roslina import Roslina
from Zwierze import Zwierze

class BarszczSosnowskiego(Roslina):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 10
        self._nazwa = "Barszcz Sosnowskiego"

    def stworzDziecko(self, x, y):
        barszczsosnowskiego = BarszczSosnowskiego(self._swiat, x, y)
        barszczsosnowskiego._nowy_organizm = True
        return barszczsosnowskiego

    def rysowanie(self):
        return (255, 0, 21)

    def czyTrujacy(self):
        return True

    def akcja(self):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(len(dx)):
            new_x = self._polozenie.x + dx[i]
            new_y = self._polozenie.y + dy[i]
            if new_x >= 0 and new_y >=0 and new_y < self._swiat._rozmiar and new_y < self._swiat._rozmiar:
                from CyberOwca import CyberOwca
                if self._swiat._plansza[new_y][new_x] is not None and isinstance(self._swiat._plansza[new_y][new_x], Zwierze) and not isinstance(self._swiat._plansza[new_y][new_x], CyberOwca):
                    if not self._swiat._plansza[new_y][new_x].jestNiesmiertelny():
                        self._swiat._aplikacjaLogi.append(f'{self._swiat._plansza[new_y][new_x]._nazwa} zostal zabity przez sasiedztwo z {self._nazwa}')
                        self._swiat._plansza[new_y][new_x].umrzyj()
        super().akcja()
from BarszczSosnowskiego import BarszczSosnowskiego
from Organizm import Punkt
from Zwierze import Zwierze
from queue import Queue

class CyberOwca(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 11
        self._inicjatywa = 4
        self._nazwa = "CyberOwca"

    def stworzDziecko(self, x, y):
        owca = CyberOwca(self._swiat, x, y)
        owca._nowy_organizm = True
        return owca

    def rysowanie(self):
        return (0, 102, 255)

    def isValid(self, x,y):
        if x < 0 or y < 0 or x >= self._swiat._rozmiar or y >= self._swiat._rozmiar:
            return False
        return True

    def akcja(self):
        flaga = False
        for i in range(len(self._swiat._listaOrganizmow)):
            if isinstance(self._swiat._listaOrganizmow[i], BarszczSosnowskiego):
                flaga = True
        if not flaga:
            super().akcja()
            return
        barszcz_do_zjedzenia = self.znajdzBarszcz()
        x_docelowy, y_docelowy = barszcz_do_zjedzenia._polozenie.x, barszcz_do_zjedzenia._polozenie.y
        x_aktualny, y_aktualny = self._polozenie.x, self._polozenie.y

        if x_docelowy > x_aktualny:
            self.wykonajRuch(x_aktualny+1, y_aktualny)
        elif x_docelowy < x_aktualny:
            self.wykonajRuch(x_aktualny-1, y_aktualny)
        elif y_docelowy > y_aktualny:
            self.wykonajRuch(x_aktualny, y_aktualny+1)
        elif y_docelowy < y_aktualny:
            self.wykonajRuch(x_aktualny, y_aktualny-1)
        return


    def znajdzBarszcz(self):
        visited = [[False] * self._swiat._rozmiar for i in range(self._swiat._rozmiar)]
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, 1, -1]
        q = Queue()
        q.put(self._polozenie)
        visited[self._polozenie.y][self._polozenie.y] = True
        while not q.empty():
            polozenie = q.get()
            x = polozenie.x
            y = polozenie.y
            for i in range(4):
                nx = x + dRow[i]
                ny = y + dCol[i]
                if self.isValid(nx, ny) and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    if (isinstance(self._swiat._plansza[ny][nx], BarszczSosnowskiego)):
                        return self._swiat._plansza[ny][nx]
                    else:
                        q.put(Punkt(nx, ny))

    def kolizja(self, organizmAtakowany):
        if (isinstance(organizmAtakowany, BarszczSosnowskiego)):
            organizmAtakowany.umrzyj()
            print(self._swiat._listaOrganizmow)
            self.wykonajRuch(organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y)
        else:
            super().kolizja()



import random

from Organizm import Organizm
from Organizm import Punkt


class Zwierze(Organizm):
    _zasieg = 1

    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)

    def znajdzPustePole(self):
        x_docelowy = self._polozenie.x
        y_docelowy = self._polozenie.y
        kierunki = []
        n = self._zasieg
        if self._polozenie.x + n <= self._swiat._rozmiar - n:
            kierunki.append(0)
        if self._polozenie.x - n >= 0:
            kierunki.append(1)
        if self._polozenie.y + n <= self._swiat._rozmiar - n:
            kierunki.append(2)
        if self._polozenie.y - n >= 0:
            kierunki.append(3)
        random_dir = kierunki[random.randint(0, len(kierunki) - 1)]
        if random_dir == 0:
            x_docelowy+=n
        if random_dir == 1:
            x_docelowy-=n
        if random_dir == 2:
            y_docelowy+=n
        if random_dir == 3:
            y_docelowy-=n
        return Punkt(x_docelowy, y_docelowy)

    def akcja(self):
        self._wiek +=1
        docelowe_kordy = self.znajdzPustePole()
        pole_docelowe = self._swiat._plansza[docelowe_kordy.y][docelowe_kordy.x]
        if self.czyMaDobryWech():
            while pole_docelowe is not None and  pole_docelowe._sila > self._sila:
                docelowe_kordy = self.znajdzPustePole()
                pole_docelowe = self._swiat._plansza[docelowe_kordy.y][docelowe_kordy.x]
        elif docelowe_kordy.x == -1:
            return
        if pole_docelowe is not None:
            self._swiat._aplikacja.dodajLog(f'Proba ruchu {self._nazwa} {self._polozenie.x, self._polozenie.y} -> {docelowe_kordy.x, docelowe_kordy.y}')
            self.kolizja(pole_docelowe)
        else:
            self.wykonajRuch(docelowe_kordy.x, docelowe_kordy.y)
            self._swiat._aplikacja.dodajLog(f'Ruch {self._nazwa} {self._polozenieWczesniejsze.x, self._polozenieWczesniejsze.y} -> {docelowe_kordy.x, docelowe_kordy.y}')

    def kolizja(self, organizmAtakowany):
        #rozmnazanie
        if type(self) is type(organizmAtakowany):
            if(self._wiek >= 5 and organizmAtakowany._wiek >= 5):
                self.rozmnoz()
                return
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - {self._nazwa} - rozmnazanie zakonczone niepowodzeniem, za mlode organizmy')
            return
        #walka
        if organizmAtakowany.dodajeSile(self):
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - {self._nazwa} - zjada Guarane i zwieksza poziom sily na pozycji {organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y}. Aktualna sila: {self._sila}')
            organizmAtakowany.umrzyj()
            self.wykonajRuch(organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y)
            return
        if organizmAtakowany.czyTrujacy() and not self.jestNiesmiertelny():
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - {self._nazwa} - zjada {organizmAtakowany._nazwa} i ginie na pozycji {organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y}')
            organizmAtakowany.umrzyj()
            self.umrzyj()
            return
        if organizmAtakowany.czyOdpartoAtak(self):
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - {organizmAtakowany._nazwa} odbija atak {self._nazwa} na pozycji {organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y}')
            return
        if organizmAtakowany.czyUcieczka(self) or self.czyUcieczka(organizmAtakowany):
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - antylopa ucieka od walki')
            return
        if self._sila >= organizmAtakowany._sila:
            if organizmAtakowany.jestNiesmiertelny():
                nowa_pozycja = organizmAtakowany.losujKierunekNiezajety()
                if nowa_pozycja.x == -1 or nowa_pozycja.y == -1:
                    self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - Czlowiek jest niesmiertelny lecz nie ma miejsca na zmiane polozenia')
                    return
                self.wykonajRuch(organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y)
                organizmAtakowany.wykonajRuch(nowa_pozycja.x, nowa_pozycja.y)
                self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - Czlowiek jest niesmiertelny - nowa pozycja {nowa_pozycja.x, nowa_pozycja.y}')
                return
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - {self._nazwa} zabija {organizmAtakowany._nazwa} na pozycji {organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y}')
            organizmAtakowany.umrzyj()
            self.wykonajRuch(organizmAtakowany._polozenie.x, organizmAtakowany._polozenie.y)
            return
        else:
            if self.jestNiesmiertelny():
                nowa_pozycja = self.losujKierunekNiezajety()
                if nowa_pozycja.x == -1 or nowa_pozycja.y == -1:
                    self._swiat._aplikacja.dodajLog(
                        f'Rezultat ruchu - Czlowiek jest niesmiertelny lecz nie ma miejsca na zmiane polozenia')
                    return
                self.wykonajRuch(nowa_pozycja.x, nowa_pozycja.y)
                self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - Czlowiek jest niesmiertelny - nowa pozycja {nowa_pozycja.x, nowa_pozycja.y}')
                return
            self._swiat._aplikacja.dodajLog(f'Rezultat ruchu - {organizmAtakowany._nazwa} zabija {self._nazwa} na pozycji {self._polozenie.x, self._polozenie.y}')
            self.umrzyj()


    def czyMaDobryWech(self):
        return False

    def wykonajRuch(self, x, y):
        self._polozenieWczesniejsze.x = self._polozenie.x
        self._polozenieWczesniejsze.y = self._polozenie.y
        self._swiat._plansza[self._polozenie.y][self._polozenie.x] = None
        self._polozenie.x = x
        self._polozenie.y = y
        self._swiat._plansza[y][x] = self

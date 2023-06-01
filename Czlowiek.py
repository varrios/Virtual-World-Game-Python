import pygame

from Organizm import Punkt
from Zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, swiat, x, y):
        super().__init__(swiat, x, y)
        self._sila = 5
        self._inicjatywa = 5
        self._nazwa = "Czlowiek"
        self._cooldown = 5
        self._niesmiertelnosc = False
        self._martwy = False
        self._czas_trwania_niesmiertelnosci = 0
        self._wybor = ''

    def stworzDziecko(self, x, y):
        return None

    def rysowanie(self):
        return (240, 113, 235)

    def akcja(self):
        if self._cooldown > 0 and not self._niesmiertelnosc:
            self._cooldown-=1
        elif self._niesmiertelnosc:
            self._czas_trwania_niesmiertelnosci-=1
            if self._czas_trwania_niesmiertelnosci == 0:
                self._cooldown = 5
                self._czas_trwania_niesmiertelnosci = 0
                self._niesmiertelnosc = False
        self._polozenieWczesniejsze = Punkt(self._polozenie.x, self._polozenie.y)
        nowe_polozenie = Punkt(self._polozenie.x, self._polozenie.y)
        znak = self._wybor
        if znak == pygame.K_DOWN:
            nowe_polozenie.y += 1
        elif znak == pygame.K_UP:
            nowe_polozenie.y -= 1
        elif znak == pygame.K_RIGHT:
            nowe_polozenie.x += 1
        elif znak == pygame.K_LEFT:
            nowe_polozenie.x -= 1
        if nowe_polozenie.x < 0 or nowe_polozenie.y < 0 or nowe_polozenie.x >= self._swiat._rozmiar or nowe_polozenie.y >= self._swiat._rozmiar:
            return
        drugi_organizm = self._swiat._plansza[nowe_polozenie.y][nowe_polozenie.x]
        if drugi_organizm is not None:
            self._swiat._aplikacjaLogi.append(f"Proba ruchu Czlowieka {self._polozenieWczesniejsze.x, self._polozenieWczesniejsze.y} -> {nowe_polozenie.x, nowe_polozenie.y}")
            super().kolizja(drugi_organizm)
        else:
            self.wykonajRuch(nowe_polozenie.x, nowe_polozenie.y)
            self._swiat._aplikacjaLogi.append(f"Ruch Czlowieka {self._polozenieWczesniejsze.x, self._polozenieWczesniejsze.y} -> {nowe_polozenie.x, nowe_polozenie.y}")

    def jestNiesmiertelny(self):
        return self._niesmiertelnosc


    def umrzyj(self):
        self._martwy = True
        super().umrzyj()

    def uzyjUmiejetnosci(self):
        if self._cooldown == 0 and not self._niesmiertelnosc:
            self._niesmiertelnosc = True
            self._czas_trwania_niesmiertelnosci = 5
            self._cooldown = 5
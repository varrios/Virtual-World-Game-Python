from copy import copy

from Antylopa import Antylopa
from BarszczSosnowskiego import BarszczSosnowskiego
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from Owca import Owca
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Wilk import Wilk
from Zolw import Zolw


class Swiat:

    def __init__(self):
        self._rozmiar = 20
        self._listaOrganizmow = []
        self._iloscOrganizmow = 0
        self._tura = 0
        self._aplikacja = None
        self._plansza = [[None] * self._rozmiar for i in range(self._rozmiar)]
        self.populuj()
        self._czlowiek = None

    def dodajOrganizm(self, organism):
        self._listaOrganizmow.append(organism)
        self._plansza[organism._polozenie.y][organism._polozenie.x] = organism
        self._iloscOrganizmow = len(self._listaOrganizmow)

    def populuj(self):
        self.dodajOrganizm(Antylopa(self, 1, 1))
        self.dodajOrganizm(Owca(self, 19, 0))
        self.dodajOrganizm(Wilk(self, 15, 2))
        self.dodajOrganizm(Zolw(self, 12, 3))
        self.dodajOrganizm(Trawa(self, 1, 10))
        self.dodajOrganizm(WilczeJagody(self, 1, 12))
        self.dodajOrganizm(Trawa(self, 1, 10))
        self.dodajOrganizm(Mlecz(self, 10, 10))
        self.dodajOrganizm(Guarana(self, 10, 10))
        self.dodajOrganizm(Lis(self, 5, 19))
        self.dodajOrganizm(BarszczSosnowskiego(self, 6, 19))

    def wykonajTure(self):
        self._iloscOrganizmow = len(self._listaOrganizmow)
        self._listaOrganizmow.sort(key=lambda o: (-o._inicjatywa, -o._wiek))
        for org in self._listaOrganizmow:
            if org._nowy_organizm:
                org._nowy_organizm = False
                continue
            org.akcja()
        self._tura += 1

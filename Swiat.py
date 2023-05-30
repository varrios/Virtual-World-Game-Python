from copy import copy

from Antylopa import Antylopa
from Owca import Owca
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

    def dodajOrganizm(self, organism):
        self._listaOrganizmow.append(organism)
        self._plansza[organism._polozenie.y][organism._polozenie.x] = organism
        self._iloscOrganizmow = len(self._listaOrganizmow)

    def populuj(self):
        #self.dodajOrganizm(Owca(self, 19, 19))
        #self.dodajOrganizm(Owca(self, 0, 19))
        #self.dodajOrganizm(Wilk(self, 0, 0))
        self.dodajOrganizm(Antylopa(self, 0, 1))
        self.dodajOrganizm(Owca(self, 0, 0))
        self.dodajOrganizm(Owca(self, 0, 2))
        self.dodajOrganizm(Zolw(self, 0, 3))

    def wykonajTure(self):
        self._iloscOrganizmow = len(self._listaOrganizmow)
        self._listaOrganizmow.sort(key=lambda o: (-o._inicjatywa, -o._wiek))
        for org in self._listaOrganizmow:
            if org._nowy_organizm:
                org._nowy_organizm = False
                continue
            print(f'{org._nazwa}')
            org.akcja()
        self._tura += 1

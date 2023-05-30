from copy import copy

from Owca import Owca


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
        self.dodajOrganizm(Owca(self, 19, 19))
        self.dodajOrganizm(Owca(self, 0, 19))
        self.dodajOrganizm(Owca(self, 17, 19))
        self.dodajOrganizm(Owca(self, 18, 19))
        for org in self._listaOrganizmow:
            print(f'{org._polozenie.x, org._polozenie.y}')

    def wykonajTure(self):
        self._iloscOrganizmow = len(self._listaOrganizmow)
        self._listaOrganizmow.sort(key=lambda o: (o._inicjatywa, o._wiek))
        for org in self._listaOrganizmow:
            if org._nowy_organizm:
                org._nowy_organizm = False
                continue
            org.akcja()
        self._tura += 1

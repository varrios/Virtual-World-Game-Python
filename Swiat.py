class Swiat:
    _plansza = []
    _rozmiar = 20
    _listaOrganizmow = []
    _iloscOrganizmow = 0
    _tura = -1
    _aplikacja = None

    def __init__(self):
        self._plansza = [[None] * self._rozmiar for i in range(self._rozmiar)]

    def dodajOrganizm(self, organism):
        self._listaOrganizmow.append(organism)
        self._plansza[organism.getY()][organism.getX()] = organism
        self._iloscOrganizmow = len(self._listaOrganizmow)

    def populuj(self):
        pass

    def wykonajTure(self):
        self._iloscOrganizmow = len(self._listaOrganizmow)
        self._listaOrganizmow.sort(key=lambda o: (o.inicjatywa, o.wiek))
        for org in self._listaOrganizmow:
            if org.stanOrganizmu:
                org.stanOrganizmu = False
                continue
            org.akcja()
        self._tura += 1

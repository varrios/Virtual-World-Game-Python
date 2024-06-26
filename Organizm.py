from abc import ABC, abstractmethod
from dataclasses import dataclass
import random


@dataclass
class Punkt:
    x: int
    y: int


class Organizm(ABC):

    def __init__(self, swiat, x, y):
        self._nazwa = "Organizm"
        self._nowy_organizm = False
        self._sila = 0
        self._inicjatywa = 0
        self._wiek = 0
        self._polozenie = Punkt(x, y)
        self._polozenieWczesniejsze = Punkt(x, y)
        self._swiat = swiat

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, organizmAtakowany):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

    @abstractmethod
    def stworzDziecko(self, x, y):
        pass

    def losujKierunekNiezajety(self):
        directions = []
        board = self._swiat._plansza
        if (self._polozenie.x + 1 <= self._swiat._rozmiar - 1) and (
                board[self._polozenie.y][self._polozenie.x + 1] is None):
            directions.append(0)
        if (self._polozenie.x - 1 >= 0) and (board[self._polozenie.y][self._polozenie.x - 1] is None):
            directions.append(1)
        if (self._polozenie.y + 1 <= self._swiat._rozmiar - 1) and (
                board[self._polozenie.y + 1][self._polozenie.x] is None):
            directions.append(2)
        if (self._polozenie.y - 1 >= 0) and (board[self._polozenie.y - 1][self._polozenie.x] is None):
            directions.append(3)
        if len(directions) == 0:
            return Punkt(-1, -1)
        random_dir = directions[random.randint(0, len(directions) - 1)]
        child_x = self._polozenie.x
        child_y = self._polozenie.y
        if random_dir == 0:
            child_x += 1
        if random_dir == 1:
            child_x -= 1
        if random_dir == 2:
            child_y += 1
        if random_dir == 3:
            child_y -= 1

        return Punkt(child_x, child_y)

    def rozmnoz(self):
        child_position = self.losujKierunekNiezajety()
        if child_position.x == -1 or child_position.y == -1:
            self._swiat._aplikacjaLogi.append(f'Rezultat ruchu - {self._nazwa} - rozmnazanie nieudane - za malo miejsca')
            return
        child = self.stworzDziecko(child_position.x, child_position.y)
        child.stanOrganizmu = True
        self._swiat.dodajOrganizm(child)
        self._swiat._aplikacjaLogi.append(
            f'Rezultat ruchu - {self._nazwa} - rozmnazanie udane - pozycja dziecka {child_position.x, child_position.y}')

    def umrzyj(self):
        self._swiat._plansza[self._polozenie.y][self._polozenie.x] = None
        self._swiat._listaOrganizmow.remove(self)

    def czyUcieczka(self, predator):
        return False

    def czyOdpartoAtak(self, predator):
        return False

    def dodajeSile(self, predator):
        return False

    def czyTrujacy(self):
        return False

    def jestNiesmiertelny(self):
        return False

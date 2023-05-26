from dataclasses import dataclass
from abc import ABC, abstractmethod
from World import *
import random


@dataclass
class Point:
    x: int
    y: int


class Organism(ABC):
    _name = "Organism"
    _courage = 0
    _strength = 0
    _age = 0
    _position = Point(0, 0)
    _previousPosition = Point(0, 0)
    _world = None
    _newOrganism = False

    def __init__(self, x, y, world):
        self._world = world
        self._position.x = x
        self._position.y = y

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, victim):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def createChild(self, x, y):
        pass

    def chooseRandomEmptyPosition(self):
        directions = []
        board = self._world.getBoard()
        if (self._position.x + 1 <= self._world.getSize() - 1) and (
                board[self._position.y][self._position.x + 1] is None):
            directions.append(0)
        if (self._position.x - 1 >= 0) and (board[self._position.y][self._position.x - 1] is None):
            directions.append(1)
        if (self._position.y + 1 <= self._world.getSize() - 1) and (
                board[self._position.y + 1][self._position.x] is None):
            directions.append(2)
        if (self._position.y - 1 >= 0) and (board[self._position.y - 1][self._position.x] is None):
            directions.append(3)
        if len(directions) == 0:
            return Point(-1, -1)
        random_dir = directions[random.randint(0, len(directions) - 1)]
        child_x = self._position.x
        child_y = self._position.y
        if random_dir == 0:
            child_x += 1
        if random_dir == 1:
            child_x -= 1
        if random_dir == 2:
            child_y += 1
        if random_dir == 3:
            child_y -= 1

        return Point(child_x, child_y)

    def breed(self):
        child_position = self.chooseRandomEmptyPosition()
        if child_position.x == -1 or child_position.y == -1:
            # print info to the logs
            return
        child = self.createChild(child_position.x, child_position.y)
        child.setStatus(True)
        self._world.addOrganism(child)
        # print info about children added to the logs

    def die(self):
        self._world.getBoard[self.getY()][self.getX()] = None
        self._world.getOrganisms().



    def escape(self, predator):
        return False

    def deflectAttack(self, predator):
        return False

    def buffs(self, predator):
        return False

    def poisonous(self):
        return False

    def invicible(self):
        return False



    # SETTERS
    def setStrength(self, strength):
        self._strength = strength

    def setCourage(self, courage):
        self._courage = courage

    def setX(self, x):
        self._position.x = x

    def setY(self, y):
        self._position.y = y

    def setStatus(self, status):
        self._newOrganism = status

    #  GETTERS
    def getX(self):
        return self._position.x

    def getY(self):
        return self._position.y

    def getStrength(self):
        return self._strength

    def getCourage(self):
        return self._courage

    def getAge(self):
        return self._strength

    def getWorld(self):
        return self._world

    def getStatus(self):
        return self._newOrganism

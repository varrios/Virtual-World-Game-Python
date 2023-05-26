class World:
    _board = []
    _organisms = []
    _organism_count = 0
    _round_no = 0

    def __init__(self, size):
        self._size = size
        self._board = [ [None]*size for i in range(size)]

    def getBoard(self):
        return self._board

    def getSize(self):
        return self._size

    def getOrganisms(self):
        return self._organisms

    def addOrganism(self, organism):
        self._organisms.append(organism)
        self._board[organism.getY()][organism.getX()] = organism
        self._organism_count = len(self._organisms)

from enum import Enum
from enum import auto

class Direction(Enum):

    NORTH = auto()
    SOUTH = auto()
    EAST  = auto()
    WEST  = auto()


all_nodes = []

class Node:

    rows = 0
    columns = 0

    directions = {'F': [Direction.SOUTH, Direction.EAST],
                  '7': [Direction.SOUTH, Direction.WEST],
                  'J': [Direction.NORTH, Direction.WEST],
                  'L': [Direction.NORTH, Direction.EAST],
                  '|': [Direction.NORTH, Direction.SOUTH],
                  '-': [Direction.EAST, Direction.WEST],
                  'S': None,
                  '.': None }

    def get_node_at(column, row):
        matches = [node for node in all_nodes if node.row == row and node.column == column]

        if len(matches) > 1:
            raise 'Too many matches'

        return matches[0]


    def __init__(self, row, column, type):

        self.row = int(row)
        self.column = int(column)
        self.type = type

        if self.type in ['.', 'S']:
            self.directions = []
        else:
            self.directions = Node.directions[type]

        if self.row > Node.rows:
            Node.rows = self.row

        if self.column > Node.columns:
            Node.columns = self.column

        all_nodes.append(self)

    def get_node_to_the(self, direction):

        if direction == Direction.NORTH and self.row > 0:
            node_north = Node.get_node_at(self.column, self.row - 1)
            if Direction.SOUTH in node_north.directions:
                return node_north

        elif direction == Direction.SOUTH and self.row < Node.rows:
            node_south = Node.get_node_at(self.column, self.row + 1)
            if Direction.NORTH in node_south.directions:
                return node_south

        elif direction == Direction.EAST and self.column < Node.columns:
            node_east = Node.get_node_at(self.column + 1, self.row)
            if Direction.WEST in node_east.directions:
                return node_east

        elif direction == Direction.WEST and self.column > 0:
            node_west = Node.get_node_at(self.column - 1, self.row)
            if Direction.EAST in node_west.directions:
                return node_west

        return None


    def get_connecting_nodes(self):

        connecting_nodes = {}

        connecting_nodes[Direction.NORTH] = self.get_node_to_the(Direction.NORTH)
        connecting_nodes[Direction.SOUTH] = self.get_node_to_the(Direction.SOUTH)
        connecting_nodes[Direction.EAST] = self.get_node_to_the(Direction.EAST)
        connecting_nodes[Direction.WEST] = self.get_node_to_the(Direction.WEST)

        for direction in Direction:
            if connecting_nodes[direction] is None:
                del connecting_nodes[direction]

        return connecting_nodes

    def get_next_node(self, lastNode):

        neighbours = [self.get_node_to_the(direction) for direction in self.directions]

        neighbours.remove(lastNode)

        return neighbours[0]


def get_input(filename):

    nodes = []

    with open(filename) as inputFile:
        raw_input = [(line.strip()) for line in inputFile]

    for row, line in enumerate(raw_input):
        for column, character in enumerate(line):
            nodes.append(Node(row, column, character))

    return nodes



if __name__ == "__main__":

    nodes = get_input('input.txt')

    starting_node = None

    for node in nodes:
        if node.type == 'S':
            starting_node = node
            break

    surrounding_nodes = starting_node.get_connecting_nodes()

    starting_node.directions = [direction for direction in surrounding_nodes.keys()]

    loop = [starting_node, list(surrounding_nodes.values())[0]]

    while loop[-1].type != 'S':
        loop.append(loop[-1].get_next_node(loop[-2]))


    print('Answer: ' + str(len(loop) // 2))


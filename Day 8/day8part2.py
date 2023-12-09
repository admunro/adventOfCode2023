import re
import math



class Node:

    all_nodes = {}

    def get_nodes_ending_in(character):
        return [node for node in Node.all_nodes.values() if node.location[2] == character]


    def __init__(self, location_string, left_string, right_string):
        self.location = location_string
        self.left = left_string
        self.right = right_string

        Node.all_nodes[self.location] = self

    def get_next_location(self, direction):
        if direction == 'L':
            return Node.all_nodes[self.left]
        elif direction == 'R':
            return Node.all_nodes[self.right]

def get_node_endings(nodes):

    return [node.location[2] for node in nodes]

def get_input(filename):
    with open(filename) as inputFile:
        raw_input = [(line.strip()) for line in inputFile]

    instructions = raw_input[0]

    nodes = []

    for line in raw_input[2:]:
        matches = re.findall('[\dA-Z]{3}', line)
        nodes.append(Node(matches[0], matches[1], matches[2]))

    return instructions, nodes


def get_path_frequency(node, instructions):

    steps = 0
    current_node = node

    while True:

        for instruction in instructions:
            steps += 1
            current_node = current_node.get_next_location(instruction)

            if current_node.location[2] == 'Z':
                return steps


if __name__ == "__main__":

    instructions, nodes = get_input('input.txt')

    starting_nodes = Node.get_nodes_ending_in('A')

    path_lengths = [get_path_frequency(node, instructions) for node in starting_nodes]

    print('Answer: ' + str(math.lcm(*path_lengths)))

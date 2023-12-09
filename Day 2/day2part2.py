import re

test_input = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
              'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
              'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
              'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
              'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

tile_colour_regex = re.compile('red|green|blue')
tile_amount_regex = re.compile('\d+')


def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]


def parse_game(turns):

    game = {'red': 0, 'green': 0, 'blue': 0}

    for turn in turns.split(';'):
        for tile in turn.split(','):
            colour = re.findall(tile_colour_regex, tile)[0]
            amount = int(re.findall(tile_amount_regex, tile)[0])

            if game[colour] < amount:
                game[colour] = amount

    return game


def parse_games(puzzle_input):

    games = {}

    for line in puzzle_input:
        raw_game = line.split(':')
        game_number = int(raw_game[0].replace('Game ', ''))
        games[game_number] = parse_game(raw_game[1])

    return games


def get_power(game):
    return game['red'] * game['green'] * game['blue']


def get_powers(games):
    return [get_power(game) for game in games.values()]


if __name__ == "__main__":

    print("Advent of Code 2023 Day 2, part 1")

    powers = get_powers(parse_games(get_input('input.txt')))

    print('The sum of the game powers is: ' + str(sum(powers)))
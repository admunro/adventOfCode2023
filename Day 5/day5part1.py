def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]


def get_seeds(puzzle_input):
    return [int(item) for item in puzzle_input[0].split() if item.isdigit()]

def parse_ranges(map_ranges):

    ranges = {}

    for map in map_ranges:
        destination_range_start = map[0]
        source_range_start = map[1]
        range_length = map[2]

        for value in range(range_length):
            ranges[source_range_start + value] = destination_range_start + value

    return ranges


def apply_map(source_number, maps):

    DESTINATION = 0
    SOURCE = 1
    RANGE_LENGTH = 2

    for map in maps:
        lower_limit = map[SOURCE]
        upper_limit = map[SOURCE] + map[RANGE_LENGTH] - 1

        if source_number >= lower_limit and source_number <= upper_limit:
            result = map[DESTINATION] + source_number - lower_limit
            return result

    return source_number




def get_map(puzzle_input, search_string):
    for index, line in enumerate(puzzle_input):
        if line == search_string:
            cursor = index + 1
            numbers = []
            while cursor < len(puzzle_input) and puzzle_input[cursor] != '':
                numbers.append([int(number) for number in puzzle_input[cursor].split()])
                cursor += 1

            return numbers


if __name__ == "__main__":

    puzzle_input = get_input('input.txt')

    seeds = get_seeds(puzzle_input)

    seed_to_soil_map = get_map(puzzle_input, 'seed-to-soil map:')
    soil_to_fertilizer_map = get_map(puzzle_input, 'soil-to-fertilizer map:')
    fertilizer_to_water_map = get_map(puzzle_input, 'fertilizer-to-water map:')
    water_to_light_map = get_map(puzzle_input, 'water-to-light map:')
    light_to_temperature_map = get_map(puzzle_input, 'light-to-temperature map:')
    temperature_to_humidity_map = get_map(puzzle_input, 'temperature-to-humidity map:')
    humidity_to_location_map = get_map(puzzle_input, 'humidity-to-location map:')

    soils = [apply_map(seed, seed_to_soil_map) for seed in seeds]

    fertilizers = [apply_map(soil, soil_to_fertilizer_map) for soil in soils]

    waters = [apply_map(fertilizer, fertilizer_to_water_map) for fertilizer in fertilizers]

    lights = [apply_map(water, water_to_light_map) for water in waters]

    temperatures = [apply_map(light, light_to_temperature_map) for light in lights]

    humidities = [apply_map(temperature, temperature_to_humidity_map) for temperature in temperatures]

    locations = [apply_map(humidity, humidity_to_location_map) for humidity in humidities]


    print('Answer: ' + str(min(locations)))
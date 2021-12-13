'''
problem:
    - 100 octopuses arranged in a 10 x 10 grid
    - at each tick, energy levels increase by 1
        - any octopus with energy level > 9 flashes
        - increases energy of adjacent octopuses by 1, including diagonal
        - an octopus can flash at most once per step
    - after flashing, energy = 0
    - predict number of flashes after 100 ticks

assumptions:
    - energy level between 0 and 9 (non-inclusive)
'''


def parse(input_str):
    return list(map(lambda x: list(map(int, list(x))), input_str.splitlines()))


def increment(row, col, matrix, incremented_neighbours):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    matrix[row][col] += 1
    if matrix[row][col] > 9 and (row, col) not in incremented_neighbours:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0),
                      (1, -1), (1, 1), (-1, 1), (-1, -1))
        incremented_neighbours.add((row, col))
        for dRow, dCol in directions:
            increment(row + dRow, col + dCol, matrix, incremented_neighbours)


def count_and_reset_above_nines(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 9:
                count += 1
                matrix[row][col] = 0
    return count


def tick(matrix):
    incremented_neighbours = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            increment(row, col, matrix, incremented_neighbours)
    return count_and_reset_above_nines(matrix)


def p1(ticks, matrix):
    count = 0
    for _ in range(ticks):
        count += tick(matrix)
    return count


def p2(matrix):
    steps = 1
    while tick(matrix) != 100:
        steps += 1
    return steps


def main():
    sample_input = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526\
'''
    parsed_sample = parse(sample_input)

    actual_input = '''\
4134384626
7114585257
1582536488
4865715538
5733423513
8532144181
1288614583
2248711141
6415871681
7881531438\
'''
    parsed_actual = parse(actual_input)

    print('sample part 1')
    print(p1(100, parsed_sample))

    print('actual part 1')
    print(p1(100, parsed_actual))

    parsed_sample = parse(sample_input)
    parsed_actual = parse(actual_input)

    print('sample part 2')
    print(p2(parsed_sample))

    print('actual part 2')
    print(p2(parsed_actual))


main()

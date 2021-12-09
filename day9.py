from heapq import heappush, heappop

'''
problem:
    - given graph, find all low points
    - calculate risk of low points, 1 + height of low point
'''


def parse(input_string):
    return list(map(lambda x: list(map(int, list(x))), input_string.splitlines()))


def check_point(row, col, from_val, matrix):
    mat_row = len(matrix)
    mat_col = len(matrix[0])
    return True if (row < 0 or col < 0 or row >= mat_row or col >= mat_col) else from_val < matrix[row][col]


def is_low_point(row, col, matrix):
    curr_val = matrix[row][col]
    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    return all([check_point(row + dRow, col + dCol, curr_val, matrix)
                for dRow, dCol in delta])


def calc_risk(matrix):
    score = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_low_point(row, col, matrix):
                score += matrix[row][col] + 1
    return score


def find_basin_size_from_low_point(row, col, matrix, visited, prev=None):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or (row, col) in visited:
        return 0
    curr = matrix[row][col]
    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    if prev == None:
        visited.add((row, col))
        return 1 + sum([find_basin_size_from_low_point(row + dRow, col + dCol, matrix, visited, curr) for dRow, dCol in delta])
    if matrix[row][col] != 9 and matrix[row][col] > prev:
        visited.add((row, col))
        return 1 + sum([find_basin_size_from_low_point(row + dRow, col + dCol, matrix, visited, curr) for dRow, dCol in delta])
    return 0


def calc_basin_sizes(matrix):
    size = 1
    values = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_low_point(row, col, matrix):
                curr_size = find_basin_size_from_low_point(
                    row, col, matrix, visited=set())
                heappush(values, -curr_size)
    for _ in range(3):
        size *= -heappop(values)
    return size


def main():
    sample_input = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
    parsed_sample = parse(sample_input)

    print('sample part 1')
    print(calc_risk(parsed_sample))

    actual_input = open('day9-input.txt').read()
    parsed_actual = parse(actual_input)

    print('actual part 1')
    print(calc_risk(parsed_actual))

    print('sample part 2')
    print(calc_basin_sizes(parsed_sample))

    print('actual part 2')
    print(calc_basin_sizes(parsed_actual))


main()

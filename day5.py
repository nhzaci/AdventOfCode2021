from collections import defaultdict

'''
problem:
    - find out the number of points where at least two points overlap
    - consider only horizontal and vertical lines
'''


class HydrothermalPart1:
    def __init__(self, proper_inputs):
        self.grid = defaultdict(lambda: 0)
        self.inputs = proper_inputs

    def run(self):
        for inp in self.inputs:
            self.ingest_input(inp)
        return self.calc_score()

    def calc_score(self):
        score = 0
        for point, val in self.grid.items():
            if val >= 2:
                score += 1
        return score

    def ingest_input(self, grid_input):
        before, after = grid_input
        x1, y1 = before
        x2, y2 = after

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            while y1 <= y2:
                self.grid[(x1, y1)] += 1
                y1 += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            while x1 <= x2:
                self.grid[(x1, y1)] += 1
                x1 += 1
        elif y1 > y2 and x1 > x2:  # (-1, -1)
            while y2 != y1 and x2 != x1:
                self.grid[(x1, y1)] += 1
                x1, y1 = x1 - 1, y1 - 1
            self.grid[(x1, y1)] += 1
        elif y2 > y1 and x1 > x2:  # (1, -1)
            while y2 != y1 and x2 != x1:
                self.grid[(x1, y1)] += 1
                x1, y1 = x1 - 1, y1 + 1
            self.grid[(x1, y1)] += 1
        elif y1 > y2 and x2 > x1:  # (-1, 1)
            while y2 != y1 and x2 != x1:
                self.grid[(x1, y1)] += 1
                x1, y1 = x1 + 1, y1 - 1
            self.grid[(x1, y1)] += 1
        elif y2 > y1 and x2 > x1:  # (1, 1)
            while y2 != y1 and x2 != x1:
                self.grid[(x1, y1)] += 1
                x1, y1 = x1 + 1, y1 + 1
            self.grid[(x1, y1)] += 1
        else:
            print('case not accounted for')


def parse(input_lines):
    sanitized_inputs = []

    for line in input_lines:
        before, after = line.split('->')
        x1, y1 = list(map(int, before.split(',')))
        x2, y2 = list(map(int, after.split(',')))
        if x1 == x2 or y1 == y2:
            sanitized_inputs.append(((x1, y1), (x2, y2)))

    return sanitized_inputs


def parse2(input_lines):
    sanitized_inputs = []

    for line in input_lines:
        before, after = line.split('->')
        x1, y1 = list(map(int, before.split(',')))
        x2, y2 = list(map(int, after.split(',')))
        sanitized_inputs.append(((x1, y1), (x2, y2)))

    return sanitized_inputs


def main():
    sample_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

    sample_lines = sample_input.splitlines()
    proper_inputs = parse(sample_lines)

    print('sample 1')
    p1 = HydrothermalPart1(proper_inputs)
    print(p1.run())

    print('actual 1')
    actual_lines = open('day5-input.txt').read().splitlines()
    actual_inputs = parse(actual_lines)

    p1 = HydrothermalPart1(actual_inputs)
    print(p1.run())

    print('sample 2')
    sample_inputs2 = parse2(sample_lines)
    p2s = HydrothermalPart1(sample_inputs2)
    print(p2s.run())

    print('actual 2')
    actual_inputs2 = parse2(actual_lines)
    p2 = HydrothermalPart1(actual_inputs2)
    print(p2.run())


if __name__ == '__main__':
    main()

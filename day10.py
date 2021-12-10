'''
problem - part 1:
    - find first illegal character in a line and add score
    - if simply incomplete, ignore for now
'''

from collections import deque

points_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_points_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

bracket_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def parse(input_str):
    return input_str.splitlines()


def calc_points1(inputs):
    score = 0
    for i in inputs:
        res, _ = check_line(i)
        if res:
            score += points_table[res]
    return score


def check_line(line):
    stack = deque([])
    for char in line:
        if char in bracket_pairs:
            stack.append(bracket_pairs[char])
        else:
            if not len(stack) or stack.pop() != char:
                return (char, [])
    return ('', stack)


def calc_autocomplete_points(inputs):
    scores = []
    for i in inputs:
        res, stack = check_line(i)
        if res == '':
            score = 0
            while stack:
                score = score * 5 + \
                    autocomplete_points_table[stack.pop()]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


def main():
    sample_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''
    parsed_sample = parse(sample_input)

    print('sample part 1')
    print(calc_points1(parsed_sample))

    actual_input = open('day10-input.txt').read()
    parsed_actual = parse(actual_input)

    print('actual part 1')
    print(calc_points1(parsed_actual))

    print('sample part 2')
    print(calc_autocomplete_points(parsed_sample))

    print('actual part 2')
    print(calc_autocomplete_points(parsed_actual))


main()

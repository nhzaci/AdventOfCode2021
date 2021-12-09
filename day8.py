'''
problem:
    - four-digit seven-segment displays in submarine are malfunctioning
    - each digit is rendered by turning on / off seven segments, a through g
    - signals have been mixed up on each display, wire segments are connected randomly
        - all digits within a display user the same connections though
'''

character_map = {
    '0': {'a', 'b', 'c', 'e', 'f', 'g'},
    '1': {'c', 'f'},
    '2': {'a', 'c', 'd', 'e', 'g'},
    '3': {'a', 'c', 'd', 'f', 'g'},
    '4': {'b', 'c', 'd', 'f'},
    '5': {'a', 'b', 'd', 'f', 'g'},
    '6': {'a', 'b', 'd', 'e', 'f', 'g'},
    '7': {'a', 'c', 'f'},
    '8': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    '9': {'a', 'b', 'c', 'd', 'f', 'g'}
}

character_length_map = {len(v): k for k, v in character_map.items() if k in {
    '1', '4', '7', '8'}}


def parse(input_string):
    line_split = input_string.splitlines()
    split_div = list(map(lambda x: x.split(' | '), line_split))
    return list(map(lambda x: list(map(lambda y: y.split(' '), x)), split_div))


def count_1_4_7_8(input_list):
    count = 0
    for _, results in input_list:
        for r in results:
            if len(r) in character_length_map:
                count += 1
    return count


def parse_part2(input_string):
    line_split = input_string.splitlines()
    split_div = list(map(lambda x: x.split(' | '), line_split))
    result = []
    for table, number in split_div:
        table_dict = {}
        number_lst = []

        for item in table.split(' '):
            key = len(item)
            table_dict[key] = table_dict.get(key, []) + [frozenset(item)]

        for n in number.split(' '):
            number_lst.append(frozenset(n))
        result.append((table_dict, number_lst))

    return result


def part2(input_list):
    s = 0
    for table, number in input_list:
        one = table[2][0]
        four = table[4][0]
        seven = table[3][0]
        eight = table[7][0]

        char_table = {
            one: 1,
            four: 4,
            seven: 7,
            eight: 8
        }

        # deduce table[5] and table[6] with "unknown" characters
        remaining_table = deduce(table, one, four, seven, eight)

        char_table.update(remaining_table)

        n_str = ''
        for n_set in number:
            n_str += str(char_table[n_set])

        s += int(n_str)
    return s


def deduce(table, one, four, seven, eight):
    ret_dict = {}
    for i in table[5]:
        if calculate_overlap(i, one) == 2:
            ret_dict[i] = 3
        elif calculate_overlap(i, four) == 3:
            ret_dict[i] = 5
        else:
            ret_dict[i] = 2

    for i in table[6]:
        if calculate_overlap(i, four) == 4:
            ret_dict[i] = 9
        elif calculate_overlap(i, four) == 3 and calculate_overlap(i, one) == 2:
            ret_dict[i] = 0
        else:
            ret_dict[i] = 6

    return ret_dict


def calculate_overlap(first, second):
    return sum(map(lambda x: x in second, first))


def main():
    sample_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''
    parsed_sample = parse(sample_input)

    actual_input = open('day8-input.txt').read()
    parsed_actual = parse(actual_input)

    print('sample part 1')
    print(count_1_4_7_8(parsed_sample))

    print('actual part 1')
    print(count_1_4_7_8(parsed_actual))

    sample_input2 = parse_part2(sample_input)
    print('sample part 2')
    print(part2(sample_input2))

    actual_input2 = parse_part2(actual_input)
    print('actual part 2')
    print(part2(actual_input2))


main()

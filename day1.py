def count_increases_part1(tests: list[int]) -> int:
    # account for edge case of missing tests
    if not len(tests):
        return 0

    no_increases = 0
    # implicit assumption: tests not empty
    prev = tests[0]
    for case in tests[1:]:
        if case > prev:
            no_increases += 1
        prev = case

    return no_increases


def count_increases_part2(tests: list[int]) -> int:
    no_window_increases = 0

    left = 0
    curr_sum = 0
    prev_sum = None

    for right in range(len(tests)):
        curr_sum += tests[right]

        while right - left + 1 > 3:
            curr_sum -= tests[left]
            left += 1

        if right - left + 1 == 3 and prev_sum != None:
            if curr_sum > prev_sum:
                no_window_increases += 1
            prev_sum = curr_sum
        elif right - left + 1 == 3:
            prev_sum = curr_sum

    return no_window_increases


def main():
    tests = list(map(int, open('day1-input.txt').read().splitlines()))
    print(count_increases_part1(tests))
    print(count_increases_part2(tests))


if __name__ == '__main__':
    main()

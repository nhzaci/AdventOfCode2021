'''
problem:
    - crab submarines need to blast through a large hole for you to escape a whale
    - crabs can only move horizontally (bubble sort-ish)
    - find the min required fuel for them to collapse into 1 single position

approach:
    - brute force
        - n^2 computation, try every single position
    - 
'''


def brute_force(inputs):
    min_sum = float("inf")
    for idx in range(len(inputs)):
        acc = 0
        for i in inputs:
            acc += abs(i - idx)
        min_sum = min(min_sum, acc)
    return min_sum


def brute_force2(inputs):
    min_sum = float("inf")
    for idx in range(len(inputs)):
        acc = 0
        for i in inputs:
            acc += ap(1, 1, abs(i - idx + 1))
        min_sum = min(min_sum, acc)
    return min_sum


def ap(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)


def main():
    sample_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    actual_input = list(map(int, open('day7-input.txt').read().split(',')))

    print('brute force sample')
    print(brute_force(sample_input))

    print('brute force actual')
    print(brute_force(actual_input))

    print('brute force sample 2')
    print(brute_force2(sample_input))

    print('brute force actual 2')
    print(brute_force2(actual_input))


if __name__ == '__main__':
    main()

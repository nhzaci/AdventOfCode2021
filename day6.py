'''
description:
    - each fish creates a new one every 7 days
    - model each fish as number of days until it creates a new one
    - new lanternfish needs 2 more days -> 9 days before it can create a new one
    - zero-indexed, so 0 is 1 day -> only when it's below 0, new fish is created
    - new fishes start at 8
    - simulate how long it takes after 80 days

problem:
    - simulate how many lanternfish we get after 80 days
'''

from collections import defaultdict


class Simulator:
    def __init__(self, start):
        self.count = len(start)
        self.day = 0
        self.fish_dict = defaultdict(lambda: 0)
        for fish in start:
            self.insert_fish(fish)

    def insert_fish(self, time):
        reproduce_day = self.day + time
        self.fish_dict[reproduce_day] += 1

    def tick(self):
        # each fish on current day produces more
        curr_day_fishes = self.fish_dict[self.day]
        # reset fishes for 7 day timer
        self.fish_dict[self.day + 7] += curr_day_fishes
        # fish produced in 7 + 2 days
        self.fish_dict[self.day + 9] += curr_day_fishes
        # increase count by fishes in current day
        self.count += curr_day_fishes
        # advance day
        self.day += 1

    def simulate(self, days):
        for _ in range(days):
            self.tick()
        return self.count


def parse_input():
    raw = list(map(int, open('day6-input.txt').read().split(',')))
    return raw


def main():
    sample_input = [3, 4, 3, 1, 2]

    print('--sample part 1')
    sample_sim = Simulator(sample_input)
    print(sample_sim.simulate(80))

    actual_input = parse_input()
    print('--actual part 1')
    sim1 = Simulator(actual_input)
    print(sim1.simulate(80))

    print('--sample part 2')
    sample_sim2 = Simulator(sample_input)
    print(sample_sim2.simulate(256))

    print('--actual part 2')
    sim2 = Simulator(actual_input)
    print(sim2.simulate(256))


if __name__ == '__main__':
    main()

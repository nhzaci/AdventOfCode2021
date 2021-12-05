'''
part 1
problem:
    1. gamma rate
        - most common bit in each corresponding position is the gamma rate
    2. epsilon rate
        - least common bit in each corresponding position is the epsilon rate
        - take 1's complement of gamma for epsilon rate
    => power consumption = gamma rate * epsilon rate

assumptions:
    - valid inputs within boundaries of range

approach:
    - using a dictionary
        - O(n) insert
        - O(1) comparison between '0' and '1' for most popular character
'''

'''
part 2
problem:
    1. find oxygen generator rating
    2. find CO2 scrubber rating
    => life support rating = oxygen generator rating * CO2 scrubber rating

approach:
    - collect most common / least common ratings first
    => find oxygen generator rating
    => find co2 scrubber rating
'''




from collections import defaultdict
class Diagnostic:
    def __init__(self, results):
        self.occur_dict = defaultdict(lambda: {'1': 0, '0': 0})
        self.results = results
        self.parse_results(results)

    def parse_results(self, results):
        if not results:
            return

        result_len = len(results[0])
        for result in results:
            for x in range(result_len):
                self.occur_dict[x][result[x]] += 1

    def generate_power_consumption(self):
        gamma_rate = ''
        epsilon_rate = ''
        for position in self.occur_dict:
            if self.occur_dict[position]['0'] > self.occur_dict[position]['1']:
                gamma_rate += '0'
                epsilon_rate += '1'
            else:
                gamma_rate += '1'
                epsilon_rate += '0'

        b_gamma_rate = int(gamma_rate, 2)
        b_epsilon_rate = int(epsilon_rate, 2)

        return b_gamma_rate * b_epsilon_rate

    def get_life_support_rating(self):
        return self.get_co2_scrubber_rating() * self.get_oxygen_generator_rating()

    def get_oxygen_generator_rating(self):
        results_remaining = self.results[:]
        curr_pos = 0
        pos_dict = defaultdict(lambda: {'1': 0, '0': 0})
        while len(results_remaining) > 1:
            for result in results_remaining:
                pos_dict[curr_pos][result[curr_pos]] += 1
            one_occur = pos_dict[curr_pos]['1']
            zero_occur = pos_dict[curr_pos]['0']
            if one_occur == zero_occur:
                results_remaining = list(
                    filter(lambda x: x[curr_pos] == '1', results_remaining))
            elif one_occur > zero_occur:
                results_remaining = list(
                    filter(lambda x: x[curr_pos] == '1', results_remaining))
            else:
                results_remaining = list(
                    filter(lambda x: x[curr_pos] == '0', results_remaining))
            curr_pos += 1
        return int(results_remaining[0], 2)

    def get_co2_scrubber_rating(self):
        results_remaining = self.results[:]
        curr_pos = 0
        pos_dict = defaultdict(lambda: {'1': 0, '0': 0})
        while len(results_remaining) > 1:
            for result in results_remaining:
                pos_dict[curr_pos][result[curr_pos]] += 1
            one_occur = pos_dict[curr_pos]['1']
            zero_occur = pos_dict[curr_pos]['0']
            if one_occur == zero_occur:
                results_remaining = list(
                    filter(lambda x: x[curr_pos] == '0', results_remaining))
            elif one_occur > zero_occur:
                results_remaining = list(
                    filter(lambda x: x[curr_pos] == '0', results_remaining))
            else:
                results_remaining = list(
                    filter(lambda x: x[curr_pos] == '1', results_remaining))
            curr_pos += 1
        return int(results_remaining[0], 2)


def main():
    results = open('day3-input.txt').read().splitlines()
    sample_input = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010'
    ]

    diag = Diagnostic(results)
    print(diag.generate_power_consumption())
    print(diag.get_life_support_rating())

    print('diag sample')

    diag_sample = Diagnostic(sample_input)
    print(diag_sample.generate_power_consumption())
    print(diag_sample.get_life_support_rating())


if __name__ == '__main__':
    main()

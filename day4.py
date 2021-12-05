from collections import deque

'''
problem:
    - figure out which board wins first
    - calculate score of winning board

approach:
    - set to store all called numbers
    - check rows and columns of board against called numbers set to find which wins
'''


class BingoPart1:
    def __init__(self, numbers, boards):
        self.called_numbers = set()
        self.numbers = numbers
        self.boards = boards

    def run_game(self):
        while True:
            curr_number = self.numbers.popleft()
            self.called_numbers.add(curr_number)
            for board in self.boards:
                if self.check_rows(board) or self.check_cols(board):
                    return self.calculate_score(board, curr_number)

    def calculate_score(self, board, called_number):
        score = 0
        for row in range(5):
            for no in board[row]:
                if no not in self.called_numbers:
                    score += int(no)
        return score * int(called_number)

    def check_rows(self, board):
        for row in range(5):
            if all(map(lambda no: no in self.called_numbers, board[row])):
                return True
        return False

    def check_cols(self, board):
        for col in range(5):
            one_false = False
            for row in range(5):
                if board[row][col] not in self.called_numbers:
                    one_false = True
                    break
            if one_false:
                continue
            else:
                return True
        return False


class BingoPart2:
    def __init__(self, numbers, boards):
        self.called_numbers = set()
        self.numbers = numbers
        self.boards = boards

    def run_game(self):
        remaining_boards = self.boards
        while len(remaining_boards) > 1:
            winning_boards = []
            curr_number = self.numbers.popleft()
            self.called_numbers.add(curr_number)
            for board_idx in range(len(remaining_boards)):
                board = remaining_boards[board_idx]
                if self.check_rows(board) or self.check_cols(board):
                    winning_boards.append(board_idx)
            for idx in winning_boards[::-1]:
                del remaining_boards[idx]

        last_board = remaining_boards[0]

        while True:
            if self.check_rows(last_board) or self.check_cols(last_board):
                return self.calculate_score(last_board, curr_number)
            curr_number = self.numbers.popleft()
            self.called_numbers.add(curr_number)

    def calculate_score(self, board, called_number):
        score = 0
        for row in range(5):
            for no in board[row]:
                if no not in self.called_numbers:
                    score += int(no)
        return score * int(called_number)

    def check_rows(self, board):
        for row in range(5):
            if all(map(lambda no: no in self.called_numbers, board[row])):
                return True
        return False

    def check_cols(self, board):
        for col in range(5):
            one_false = False
            for row in range(5):
                if board[row][col] not in self.called_numbers:
                    one_false = True
                    break
            if one_false:
                continue
            else:
                return True
        return False


def parse(input_txt: deque):
    number_order = deque(input_txt.popleft().split(','))

    boards = []

    while input_txt:
        input_txt.popleft()
        board = []
        for _ in range(5):
            line = input_txt.popleft()
            board_line = []
            for x in range(5):
                start = x * 3
                end = start + 2
                board_line.append(str(int(line[start:end])))
            board.append(board_line)
        boards.append(board)

    return number_order, boards


def main():
    sample_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

    sample_lines = deque(sample_input.splitlines())

    print()
    print('sample')
    numbers_sample, boards_sample = parse(sample_lines)
    p1 = BingoPart1(numbers_sample, boards_sample)
    print(p1.run_game())

    actual_input = deque(open('day4-input.txt').read().splitlines())

    print()
    print('actual')
    numbers, boards = parse(actual_input)
    p1 = BingoPart1(numbers, boards)
    print(p1.run_game())

    sample_lines = deque(sample_input.splitlines())
    print()
    print('sample part 2')
    numbers_sample, boards_sample = parse(sample_lines)
    p2 = BingoPart2(numbers_sample, boards_sample)
    print(p2.run_game())

    actual_input = deque(open('day4-input.txt').read().splitlines())
    print()
    print('actual part 2')
    numbers, boards = parse(actual_input)
    p2 = BingoPart2(numbers, boards)
    print(p2.run_game())


if __name__ == '__main__':
    main()

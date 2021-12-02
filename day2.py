'''
problem:
    - submarine takes series of commands
        - forward X -> increase horizontal by X
        - down    X -> increases depth by X units
        - up      X -> decreases depth by X units

assumptions:
    - all inputs are positive integers
    - no invalid movements, only ['forward', 'down', 'up']
    - submarine only has a horizontal and depth component
    - minimum depth is 0, cannot go negative, since that would mean it's floating
'''


class SubmarinePart1:
    def __init__(self):
        self.horiz = 0
        self.depth = 0

    def forward(self, x):
        self.horiz += x

    def down(self, x):
        self.depth += x

    def up(self, x):
        self.depth -= x

    def process_command(self, command):
        command_txt, x = command.split(' ')
        x = int(x)

        if command_txt == 'forward':
            self.forward(x)
        elif command_txt == 'down':
            self.down(x)
        elif command_txt == 'up':
            self.up(x)

    def get_horiz_depth_product(self):
        return self.depth * self.horiz


class SubmarinePart2:
    def __init__(self):
        self.horiz = 0
        self.depth = 0
        self.aim = 0

    def forward(self, x):
        self.horiz += x
        self.depth += self.aim * x

    def down(self, x):
        self.aim += x

    def up(self, x):
        self.aim -= x

    def process_command(self, command):
        command_txt, x = command.split(' ')
        x = int(x)

        if command_txt == 'forward':
            self.forward(x)
        elif command_txt == 'down':
            self.down(x)
        elif command_txt == 'up':
            self.up(x)

    def get_horiz_depth_product(self):
        return self.depth * self.horiz


def main():
    commands = open('day2-input.txt').read().splitlines()

    part1 = SubmarinePart1()
    part2 = SubmarinePart2()

    for command in commands:
        part1.process_command(command)
        part2.process_command(command)

    print(part1.get_horiz_depth_product())
    print(part2.get_horiz_depth_product())


if __name__ == '__main__':
    main()

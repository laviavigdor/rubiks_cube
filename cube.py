# Inspired by https://codegolf.stackexchange.com/a/92806/19725
# Notation: https://ruwix.com/the-rubiks-cube/notation/advanced/
import re
from collections import Counter
from colorama import Fore, Back, Style

PERFECT_CUBE = [[color] * 9 for color in 'YBRGOW']
COLOR_MAP = {
    'G': Back.GREEN,
    'Y': Back.YELLOW,
    'W': Back.WHITE,
    'R': Back.RED,
    'O': Back.LIGHTYELLOW_EX,
    'B': Back.BLUE,
}

class Cube:
    def __init__(self):
        self.data = PERFECT_CUBE

    r = lambda self, f: [f[a + b] for a in (0, 1, 2) for b in
                         (6, 3, 0)]  # only rotates the stickers on a face, clockwise a quarter-turn
    U = lambda self, c: [self.r(c[0])] + [c[j + 1][:3] + c[j or 4][3:] for j in (1, 2, 3, 0)] + [c[5]]
    y = lambda self, c: [self.r(c[0])] + c[2:5] + [c[1], self.r(self.r(self.r(c[5])))]
    z = lambda self, c: [c[2], self.r(self.r(self.r(c[1]))), c[5], self.r(c[3]), c[0][::-1], c[4][::-1]]

    def get_commands(self, input):
        commands = "self.data=" + "(self.data);self.data=".join("".join(
            "zzzUz U zzUzz yyyzUzzzy zUzzz yzUzzzyyy".split()[ord(t) % 11 % 7] * (ord(n or 'a') % 6) for t, n in
            re.findall("([BUDLFR])(['2i]?)", input))) + "(self.data)"

        commands = commands.replace('z(', 'self.z(')
        commands = commands.replace('U(', 'self.U(')
        commands = commands.replace('y(', 'self.y(')
        return commands

    def rotate(self, input):
        commands = self.get_commands(input)
        exec (commands)

    def __str__(self):
        nine_spaces = ' ' * 9
        line_breaks = '\n'.join
        spaces = ''.join

        rows = [
            [
                nine_spaces,nine_spaces,
                self.data[0]
            ],
            self.data[1:5],
            [
                nine_spaces,nine_spaces,
                self.data[5]
            ]
        ]

        output = line_breaks(
            line_breaks(
                spaces(
                    spaces(f[w:w + 3]) for f in row
                ) for w in (0, 3, 6)
            ) for row in rows
        )

        for letter in COLOR_MAP:
            color = COLOR_MAP[letter]
            output = output.replace(letter, color + '  ' + Style.RESET_ALL)

        return output

    def grade(self):
        '''
        Sum the count of max number of same color in each face, divide by sum of perfect cube
        :return:
        '''
        the_sum = sum([Counter(face).most_common(1)[0][1] for face in self.data])
        perfect_sum = 9 * 6
        score = 100.0 * the_sum / perfect_sum
        return score
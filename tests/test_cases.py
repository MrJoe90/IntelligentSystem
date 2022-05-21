from collections import namedtuple

Box = namedtuple('Box', "x y value")

# Input Tests (Correct Structure)
word_a = ['s', 'h', 'u', 't']
initial_a = [Box(2, 0, 'u'),
             Box(1, 1, 't'),
             Box(1, 3, 'h'),
             Box(2, 2, 's')]

word_b = ['h', 'o', 'p', 'e']
initial_b = [Box(2, 0, 'e'),
             Box(1, 1, 'h'),
             Box(1, 3, 'o'),
             Box(2, 2, 'p')]

word_c = ['g', 'a', 'm', 'e']
initial_c = [Box(2, 0, 'g'),
             Box(1, 1, 'a'),
             Box(1, 3, 'm'),
             Box(2, 2, 'e')]


# Input Tests (Incorrect Structure)

word_d = ['t', 'r', 'y']
initial_d = [Box(2, 0, 'y'),
             Box(1, 1, 'r'),
             Box(1, 3, 't')]

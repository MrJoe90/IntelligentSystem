from collections import namedtuple

Box = namedtuple('Box', "x y value")

# Input Tests (Correct Structure)
word_a = ['s', 'h', 'u', 't']
initial_a = [Box(2, 0, 'u'),
             Box(1, 1, 't'),
             Box(1, 3, 'h'),
             Box(2, 2, 's')]

word_b = ['h', 'o', 'p', 'e']
initial_b = [Box(0, 0, 'e'),
             Box(0, 1, 'h'),
             Box(0, 3, 'o'),
             Box(0, 2, 'p')]

word_c = ['g', 'a', 'm', 'e']
initial_c = [Box(0, 0, 'g'),
             Box(1, 1, 'a'),
             Box(2, 2, 'm'),
             Box(3, 3, 'e')]


# Input Tests (Incorrect Structure)

word_d = ['t', 'r', 'y']
initial_d = [Box(2, 0, 'y'),
             Box(1, 1, 'r'),
             Box(1, 3, 't')]

word_e = ['w', 'o', 'r', 'd']
initial_e = [Box(0, 0, 'w'),
             Box(0, 1, 'd'),
             Box(0, 2, 'r'),
             Box(0, 3, 'o'),
             Box(1, 0, 'o'),
             Box(1, 1, 'r'),
             Box(1, 2, 'w'),
             Box(1, 3, 'd'),]

# Currently unable to test correct answer
answer_e = 0
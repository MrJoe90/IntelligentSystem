import threading
import random
from collections import namedtuple

Box = namedtuple('Box', "x y value")


class SudokuGeneticRepresentation:

    def __init__(self, words: list, initial_configuration: list):

        if len(words) > 4:
            raise TypeError("We only accept size 4x4 sudoku, sorry.")
        self._row_number = 4
        self._col_number = 4
        self._data = []
        self._position_fixed = initial_configuration
        for i in range(0, 4):
            self._data.append([random.choice(words) for j in range(0, 4)])
        # Assuming a correct input --another type error should be raised here.
        for element in initial_configuration:
            self._data[element.x][element.y] = element.value
        self._internal_use = []
        self._mapping_word_to_bit = {words[0]: (0, 0),
                                     words[1]: (0, 1),
                                     words[2]: (1, 0),
                                     words[3]: (1, 1),
                                     }
        for i in range(0, 4):
            self._internal_use.append(
                [self._mapping_word_to_bit[self._data[i][j]] for j in range(0, 4)])

    @property
    def data(self):
        return self._data

    @property
    def internal_use(self):
        return self._internal_use

    def fitness_value(self):
        row_violated = 0
        col_violated = 0
        sub_matrix_violated = 0

        # Check by row
        for i in range(0, self._data.__len__()):
            for j in range(0, self._data[i].__len__()):
                for k in range(j+1, self._data[i].__len__()):
                    if self._data[i][j] == self._data[i][k]:
                        row_violated += 1

        # Check by col
        for i in range(0, self._data.__len__()):
            for j in range(0, self._data[i].__len__()):
                for k in range(i+1, self._data[i].__len__()):
                    if self._data[j][i] == self._data[k][i]:
                        col_violated += 1

        # Check by sub-matrix
        if self._data[0][0] == self._data[1][1] or \
           self._data[1][0] == self._data[0][1]:
            sub_matrix_violated += 1

        if self._data[0][2] == self._data[1][3] or \
           self._data[1][2] == self._data[0][3]:
            sub_matrix_violated += 1

        if self._data[2][0] == self._data[3][1] or \
           self._data[3][0] == self._data[2][1]:
            sub_matrix_violated += 1

        if self._data[2][2] == self._data[3][3] or \
           self._data[3][2] == self._data[2][3]:
            sub_matrix_violated += 1

        return (row_violated, col_violated, sub_matrix_violated)

    def __str__(self):
        return self._data.__str__()


class Sudoku(threading.Thread):
    def __init__(self, number_of_generation, words: list, initial: Box):
        threading.Thread.__init__(self)
        self._number_of_generation = number_of_generation
        self._sudoku = None
        self._poupolation = [SudokuGeneticRepresentation(
            words, initial) for i in range(0, 12)]
        self._scoring = []

    def run(self):
        current_generation = 0

        while current_generation < self._number_of_generation:
            current_generation += 1

    def fitness_function(self):
        # Foreach element in the population
        ScorePoint = namedtuple('ScorePoint', " t element")

        for element in self._poupolation:
            self._scoring.append(ScorePoint(element.fitness_value(), element))
        self._scoring.sort(key=lambda ScorePoint: ScorePoint[0])

    def selection_new_couples(self):
        # I do select the most fit, since they are ordered
        couples = random.choices(self._scoring,
                                 weights=[i for i in range(
                                     len(self._scoring), 0, -1)],
                                 k=len(self._scoring)//2)
        return couples

    def crossfunction(self, couples):

        for i in range(0, len(couples), 2):
            spliting_point_one = int(random.random()*7)+3
            spliting_point_two = int(random.random()*7)+3
            first_half = list(couples[i][1].internal_use).

    def mutation(self, new_generation):
        pass


if __name__ == "__main__":

    words = ['a', 'b', 'c', 'd']
    initial = [Box(2, 0, 'c'),
               Box(1, 1, 'b'),
               Box(1, 3, 'a'),
               Box(2, 2, 'd')]

    #s = SudokuGeneticRepresentation(words, initial)
    sudoku_genitico = Sudoku(100, words, initial)
    sudoku_genitico.fitness_function()
    c = sudoku_genitico.selection_new_couples()
    sudoku_genitico.crossfunction(c)

    # sudoku_genitico.start()

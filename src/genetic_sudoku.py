import threading
import random
from collections import namedtuple
import time

from scipy import rand

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
            self._data.append(random.sample(words, k=4))
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

    @internal_use.setter
    def internal_use(self, new_one):
        self._internal_use = new_one

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
        # if row_violated <= 3 and col_violated <= 3:
        if row_violated > 3 and col_violated > 3:
            if row_violated+sub_matrix_violated >= col_violated+sub_matrix_violated:
                return row_violated+sub_matrix_violated
            else:
                return col_violated+sub_matrix_violated

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

        return (col_violated+sub_matrix_violated)

    def __str__(self):
        return self._data.__str__()

    def in_sync_with_internal_use(self):
        self._data = None
        self._data = []

        for i in range(0, 4):
            temp = []
            for j in range(0, 4):
                for k, v in self._mapping_word_to_bit.items():
                    if v == self._internal_use[i][j]:
                        temp.append(k)
                        break
            self._data.append(temp)


class Sudoku(threading.Thread):
    def __init__(self, number_of_generation, words: list, initial: Box):
        threading.Thread.__init__(self)
        self._number_of_generation = number_of_generation
        self._sudoku = None
        self._population = [SudokuGeneticRepresentation(
            words, initial) for i in range(0, 30)]
        self._scoring = []

    def run(self):
        current_generation = 0

        while current_generation < self._number_of_generation:
            self.fitness_function()
            c = self.selection_new_couples()
            self.crossfunction(c)
            current_generation += 1
            if current_generation % 5 == 0:
                # You don't have the new generation yet
                self._scoring.sort(key=lambda ScorePoint: ScorePoint[0])
                for i in range(self._scoring.__len__(), 10):
                    self._population.pop(i)

                for i in range(0, 5):
                    self._population.append(SudokuGeneticRepresentation(
                        ['a', 'b', 'c', 'd'], self._population[0]._position_fixed))

        print(time.ctime())
        self._scoring.sort(key=lambda ScorePoint: ScorePoint[0])
        print(self._scoring[0][1])
        print(self._scoring[0][0])
        print(self._scoring[1][1])
        print(self._scoring[1][0])

    def fitness_function(self):
        # Foreach element in the population
        ScorePoint = namedtuple('ScorePoint', " t element")

        self._scoring = []

        for element in self._population:
            self._scoring.append(ScorePoint(element.fitness_value(), element))

        self._scoring.sort(key=lambda ScorePoint: ScorePoint[0])

    def selection_new_couples(self):
        # I do select the most fit, since they are ordered
        if self._scoring.__len__() >= 2:

            couples = random.sample(self._scoring[0:10],
                                    k=8)
        else:
            return self._scoring

        return couples

    def crossfunction(self, couples):
        i = 0
        current_index = self._population.__len__()
        spliting_point = random.randrange(3, 8)

        while i < len(couples)//2:
            first_cromo = couples[i][1].internal_use
            second_cromo = couples[i+1][1].internal_use
            first_half_fc = []
            second_half_fc = []
            first_half_sc = []
            second_half_sc = []
            k = 0
            for i in range(0, 4):
                for j in range(0, 4):
                    if k < spliting_point:
                        first_half_fc.append(first_cromo[i][j])
                    k += 1
            k = 0
            for i in range(0, 4):
                for j in range(0, 4):
                    if k < spliting_point:
                        pass

                    else:
                        second_half_fc.append(first_cromo[i][j])
                    k += 1
            k = 0
            for i in range(0, 4):
                for j in range(0, 4):
                    if k < spliting_point:
                        first_half_sc.append(second_cromo[i][j])
                    k += 1
            k = 0
            for i in range(0, 4):
                for j in range(0, 4):
                    if k < spliting_point:
                        pass
                    else:
                        second_half_sc.append(second_cromo[i][j])
                    k += 1

            temp = self.__combine_two_pieces(first_half_fc, second_half_sc)
            self.mutation(temp)
            self._population.insert(3, temp)
            temp = self.__combine_two_pieces(first_half_sc, second_half_fc)
            self.mutation(temp)
            self._population.insert(4, temp)
            i += 2

    def __combine_two_pieces(self, first_half_fc, second_half_fc):

        new_element = []
        l = 0
        m = 0
        for i in range(0, 4):
            acc = []
            for j in range(0, 4):
                if m < len(first_half_fc):
                    acc.append(first_half_fc[m])
                    m += 1
                else:
                    acc.append(second_half_fc[l])
                    l += 1
            new_element.append(acc)

        temp = SudokuGeneticRepresentation(
            ['a', 'b', 'c', 'd'], self._population[0]._position_fixed)
        temp.internal_use = new_element
        temp.in_sync_with_internal_use()

        return temp

    def mutation(self, element: SudokuGeneticRepresentation):
        # Can mutate just the gene that are not already part of the solution
        # Because the come from the users input
        change_letter_in_row = random.randrange(0, 3)
        change_letter_in_col = random.randrange(0, 3)

        likely = random.random()
        if likely <= 0.83:
           # Check fixed position later, do not forget
            for f in element._position_fixed:
                if f[0] == change_letter_in_row and f[1] == change_letter_in_col:
                    return
            temp = set()
            for i in (0, 3):
                temp.add(element.data[change_letter_in_col][i])

            for i in (0, 3):
                temp.add(element.data[change_letter_in_row][i])

            present_words = set(element._mapping_word_to_bit.keys())
            difference = list(present_words.difference(temp))
            if len(difference) == 0:
                return
            new_letter = random.choices(difference, k=1)

            element.internal_use[change_letter_in_row][change_letter_in_col] = element._mapping_word_to_bit[difference[difference.index(
                new_letter[0])]]
            element.in_sync_with_internal_use()


if __name__ == "__main__":
    random.seed(None)
    words = ['a', 'b', 'c', 'd']
    initial = [Box(2, 0, 'c'),
               Box(1, 1, 'b'),
               Box(1, 3, 'a'),
               Box(3, 1, 'd'),
               Box(3, 2, 'a'), ]

    # s = SudokuGeneticRepresentation(words, initial)

    print(time.ctime())
    sudoku_genitico = Sudoku(315, words, initial)
    sudoku_genitico.start()

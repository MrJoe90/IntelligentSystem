from concurrent.futures import thread
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

        # (row_violated, col_violated, sub_matrix_violated)
        return (row_violated+col_violated+sub_matrix_violated)

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
            words, initial) for i in range(0, 250)]
        self._scoring = []

    def run(self):
        current_generation = 0

        while current_generation < self._number_of_generation:
            self.fitness_function()
            c = self.selection_new_couples()
            self.crossfunction(c)
            # if current_generation % 10 == 0 and self._population.__len__() >= 4:
            #    self._population.pop(self._population.__len__()//2)
            #    self._population.pop(self._population.__len__()//2)

            current_generation += 1

        print(len(self._population))
        print(self._population[0])
        print(self._population[1])
        print(self._scoring[0])
        print(self._scoring[1])

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
            couples = random.choices(self._scoring,
                                     weights=[i for i in range(
                                         len(self._scoring), 0, -1)],
                                     k=len(self._scoring))
        else:
            return self._scoring

        return couples

    def crossfunction(self, couples):
        i = 0
        last_index = self._population.__len__()

        while i < len(couples)//2:
            spliting_point = int(random.random()*2)+1
            first_cromo = couples[i][1].internal_use
            first_half_fc = first_cromo[0:spliting_point]
            second_half_fc = first_cromo[spliting_point:]
            second_cromo = couples[i+1][1].internal_use
            first_half_sc = second_cromo[0:spliting_point]
            second_half_sc = second_cromo[spliting_point:]
            temp = self.__combine_two_pieces(first_half_fc, second_half_sc)
            self.mutation(temp)
            self._population.append(temp)
            temp = self.__combine_two_pieces(first_half_sc, second_half_fc)
            self.mutation(temp)
            self._population.append(temp)
            i += 2

        for i in (last_index, last_index-len(couples), -1):
            self._population.pop(i)

    def __combine_two_pieces(self, first_half_fc, second_half_fc):
        new_element = []
        for i in first_half_fc:
            new_element.append(i)
        for i in second_half_fc:
            new_element.append(i)
        temp = SudokuGeneticRepresentation(['a', 'b', 'c', 'd'], [])
        temp.internal_use = new_element
        temp.in_sync_with_internal_use()
        return temp

    def mutation(self, element: SudokuGeneticRepresentation):
        # Can mutate just the gene that are not already part of the solution
        # Because the come from the users input
        change_letter_in_square = int(random.random()*15)
        new_letter = int(random.random()*3)

        likely = random.random()
        if likely > 0.5:
            # Check fixed position later, do not forget
            for f in element._position_fixed:
                if f[0]+f[1] == change_letter_in_square:
                    return

            element.data[int(change_letter_in_square)//4][int(
                change_letter_in_square)//4] = list(element._mapping_word_to_bit.keys())[new_letter]
            element.internal_use[int(change_letter_in_square)//4][int(
                change_letter_in_square)//4] = list(element._mapping_word_to_bit.values())[new_letter]


if __name__ == "__main__":

    words = ['a', 'b', 'c', 'd']
    initial = [Box(2, 0, 'c'),
               Box(1, 1, 'b'),
               Box(1, 3, 'a'),
               Box(2, 2, 'd')]

    # s = SudokuGeneticRepresentation(words, initial)
    sudoku_genitico = Sudoku(20, words, initial)
    sudoku_genitico.start()
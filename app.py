# Import UI packages
import re
import tkinter as tk
from tkinter import *

# Import Genetic Algorithm
from collections import namedtuple
from src.genetic_sudoku import Sudoku
import time


class SudokuApp:
    """Need to put description here"""

    def __init__(self, window):
        self.window = window
        # Run the window
        window.title('Word Sudoku')
        window.geometry("600x400")
        window.configure(bg="#ADD8E6")

        self.pixelVirtual = PhotoImage(width=1, height=1)

        # Add title to application
        self.label_one = Label(window,
                               text="Enter four letter word into the grid...",
                               fg='black',
                               font=("Helvetica", 10),
                               image=self.pixelVirtual,
                               height=30,
                               width=400,
                               compound="c")

        self.label_one.place(x=100, y=30)

        # Create and place input boxes
        format = ("Helvetica", 18)
        self.input_1 = Text(window, font=format, height=1, width=3)
        self.input_2 = Text(window, font=format, height=1, width=3)
        self.input_3 = Text(window, font=format, height=1, width=3)
        self.input_4 = Text(window, font=format, height=1, width=3)
        self.input_5 = Text(window, font=format, height=1, width=3)
        self.input_6 = Text(window, font=format, height=1, width=3)
        self.input_7 = Text(window, font=format, height=1, width=3)
        self.input_8 = Text(window, font=format, height=1, width=3)
        self.input_9 = Text(window, font=format, height=1, width=3)
        self.input_10 = Text(window, font=format, height=1, width=3)
        self.input_11 = Text(window, font=format, height=1, width=3)
        self.input_12 = Text(window, font=format, height=1, width=3)
        self.input_13 = Text(window, font=format, height=1, width=3)
        self.input_14 = Text(window, font=format, height=1, width=3)
        self.input_15 = Text(window, font=format, height=1, width=3)
        self.input_16 = Text(window, font=format, height=1, width=3)

        inputs = [(self.input_1, self.input_2, self.input_3, self.input_4),
                  (self.input_5, self.input_6, self.input_7, self.input_8),
                  (self.input_9, self.input_10, self.input_11, self.input_12),
                  (self.input_13, self.input_14, self.input_15, self.input_16)]

        x = 220
        y = 100
        for i in range(4):
            for j in range(4):
                self.table = inputs[i][j]
                self.table.place(x=x+i*40, y=y+j*40)

        # Generate the result from the grid
        def generateSudoku():
            self.show_result.configure(text="Calculating solution...")

            generations = 122
            Box = namedtuple('Box', "x y value")
            input_1 = self.input_1.get(1.0, "end-1c")
            input_2 = self.input_2.get(1.0, "end-1c")
            input_3 = self.input_3.get(1.0, "end-1c")
            input_4 = self.input_4.get(1.0, "end-1c")
            input_5 = self.input_5.get(1.0, "end-1c")
            input_6 = self.input_6.get(1.0, "end-1c")
            input_7 = self.input_7.get(1.0, "end-1c")
            input_8 = self.input_8.get(1.0, "end-1c")
            input_9 = self.input_9.get(1.0, "end-1c")
            input_10 = self.input_10.get(1.0, "end-1c")
            input_11 = self.input_11.get(1.0, "end-1c")
            input_12 = self.input_12.get(1.0, "end-1c")
            input_13 = self.input_13.get(1.0, "end-1c")
            input_14 = self.input_14.get(1.0, "end-1c")
            input_15 = self.input_15.get(1.0, "end-1c")
            input_16 = self.input_16.get(1.0, "end-1c")
            coords = [[0, 0, input_1], [1, 0, input_2],
                      [2, 0, input_3], [3, 0, input_4],
                      [0, 1, input_5], [1, 1, input_6],
                      [2, 1, input_7], [3, 1, input_8],
                      [0, 2, input_9], [1, 2, input_10],
                      [2, 2, input_11], [3, 2, input_12],
                      [0, 3, input_13], [1, 3, input_14],
                      [2, 3, input_15], [3, 3, input_16]]

            def getWords(list):
                return [item[2] for item in list if item[2] != '']

            def getPositions(list):
                return [item for item in list if item[2] != '']

            def generateInitial(list):
                return [Box(item[0], item[1], item[2]) for item in list]

            words = list(set(getWords(coords)))
            positions = getPositions(coords)
            initial = generateInitial(positions)

            print(words)
            print(positions)
            print(initial)

            if len(words) < 4:
                self.show_result.configure(text=("Please enter a minimum of "
                                                 "four unique letters."))
            elif len(words) > 4:
                self.show_result.configure(text=("Please enter a maximum of "
                                                 "four unique letters."))
            else:
                pass
            print(initial)
            solver = Sudoku(generations, words, initial)
            solver.start()
            while not solver.finish_event.is_set():
                solver.finish_event.wait(1)

            sol = solver.solution

            for i in range(0, 4):
                for j in range(0, 4):
                    inputs[j][i].delete(1.0)
                    inputs[j][i].insert(1.0, sol[i][j][2])

        self.submit_button = Button(window, text="Submit",
                                    command=generateSudoku)
        self.submit_button.place(relx=0.5, y=350, anchor=CENTER)
        self.show_result = Label(window, text="Click submit to see results.")
        self.show_result.place(relx=0.5, y=300, anchor=CENTER)


root = Tk()
app = SudokuApp(root)
root.mainloop()

# Import UI packages
import tkinter as tk
from tkinter import *

# Import Genetic Algorithm
from collections import namedtuple
from src.genetic_sudoku import Sudoku


class SudokuApp:
    """Need to put description here"""

    def __init__(self, window):
        self.window = window
        # Run the window
        window.title('Word Sudoku')
        window.geometry("600x600")
        window.configure(bg="#ADD8E6")

        self.pixelVirtual = PhotoImage(width=1, height=1)

        self.label_one = Label(window, text="Enter your four letter word...",
                               fg='black', font=("Helvetica", 10),
                               image=self.pixelVirtual, height=30,
                               width=400, compound="c")
        self.label_one.place(x=100, y=30)

        self.input_one = Text(window, font=("Helvetica", 18),
                              height=1, width=3)
        self.input_two = Text(window, font=("Helvetica", 18),
                              height=1, width=3)
        self.input_three = Text(window, font=("Helvetica", 18),
                                height=1, width=3)
        self.input_four = Text(window, font=("Helvetica", 18),
                               height=1, width=3)

        self.input_one.place(x=130, y=100)
        self.input_two.place(x=230, y=100)
        self.input_three.place(x=330, y=100)
        self.input_four.place(x=430, y=100)

        def generateSudoku():
            generations = 20
            Box = namedtuple('Box', "x y value")
            input_one = self.input_one.get(1.0, "end-1c")
            input_two = self.input_two.get(1.0, "end-1c")
            input_three = self.input_three.get(1.0, "end-1c")
            input_four = self.input_four.get(1.0, "end-1c")
            words = [input_one, input_two, input_three, input_four]
            initial = [Box(2, 0, 'c'),
                       Box(1, 1, 'b'),
                       Box(1, 3, 'a'),
                       Box(2, 2, 'd')]
            result = str(Sudoku(generations, words, initial))
            self.show_result.config(text="Result: "+result)

        self.submit_button = Button(window, text="Submit",
                                    command=generateSudoku)
        self.submit_button.place(x=200, y=200)
        self.show_result = Label(window, text="")
        self.show_result.place(x=200, y=300)


root = Tk()
app = SudokuApp(root)
root.mainloop()

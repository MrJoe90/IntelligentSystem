For this assignment, you will be divided into groups to work through the production of a genetic software system and towards a final report (2,000/2,500 words) to outline the system developed. Please use the Group Work Discussion Forum to collaborate with your group.

## Task

Create a software application that solves a puzzle game similar to Sudoku using genetic algorithms. The objective is to fill a grid of size 4x4 with four different letters so that each column, each row, and each of the four sub-grids of size 2x2 contain each of the letters only once

As an example, this is a successfully solved grid:

|   |   |   |   |
|---|---|---|---|
| W | D | R | O |
| O | R | W | D |
| R | O | D | W |
| D | W | O | R |

At the start of the game, a partially completed grid is provided by the user. Depending on the initial configuration, the puzzle might have no solution, one single solution or more than one solution. You decide the initial placement on the grid.

The conditions for letter placement on the 4x4 grid are as follows:
the four letters are all different from each other; you decide what letters to use as long as they are all different
the same single letter may not appear twice in the same row, column, or any of the four subgrids of size 2x2

To prepare for this assignment:
Review the module's resources, references, and the scenario above.
Prepare any tool that your group would use to carry out this assignment.
Estimate the work that needs to be done to complete this assignment and divide it among the members of your group. You can divide the work in many ways. You can divide the work by task, by sections of the reports, or by any other means that your group finds suitable for your needs. It may be helpful to keep a record of what you have decided.

## To complete this assignment:
You must solve the puzzle using genetic algorithms.
You must submit your system developed in pseudocode.

- Try out your code with more than one initial grid placement display the solution to the puzzle given the initial configuration show all populations created to get to that solution (if a solution is possible, given the initial configuration).
- [optional] display only the solutions that contain a specific word along the edges of the grid (e.g. if you use the four letters ‘W’,’O’,’R’,D’ you may want to show only the solutions that contain the word “WORD” along one or more edges)
- [optional] Develop your system using a programming language of your choice, and submit the source code.
Write and submit a final report (2000/2500 words) in PDF that describes and analyses your application. Specifically, discuss how you encoded your input and output data for genetic operations, how you chose the fitness function, and how you implemented the genetic operators. You also must justify your choices. Your report should provide an account of the task undertaken in a reasonably concise and practical manner and should contain
    - Title.
    - Module name
    - Name of group members who participated in this assignment
    - A brief introduction
    - A body, subdivided into sections if helpful (aim at 3-5 sections) covering different aspects of the task and its proposed solution, with a critical analysis of the decisions taken
    - A conclusion

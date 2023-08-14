# Pattern Matching with Regular Expressions

This Python program implements a pattern matching algorithm using the Knuth-Morris-Pratt (KMP) substring search algorithm and various modifications to handle special characters and patterns. The program reads pattern and text files, performs searches based on the provided patterns, and writes the matching positions to output files.

## Features

- Efficient substring matching using the KMP algorithm.
- Special pattern handling for backslashes, dots, question marks, start (^), and end ($) characters.
- Reports the line number and index of each matching position.
- Measures and displays the runtime of each search.

## Setup

1. Clone this repository to your local machine.
2. Place pattern files (e.g., `pattern1.txt`, `pattern2.txt`, etc.) inside the `Inputs/Patterns` directory.
3. Place text files (e.g., `text1.txt`, `text2.txt`, etc.) inside the `Inputs/Texts` directory.
4. Number of pattern files and text files must be same.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the program files.
3. Run the `Main.py` script by executing the command:
4. Follow the on-screen instructions to input the number of file pairs and observe the pattern matching results.
5. The matching positions and runtime information will be stored in output files located in the `Outputs` folder.

## Results

The program provides detailed results for each search, including the number of matches found, line numbers, indices, and runtime information.

## Troubleshooting

If you encounter any errors during execution, ensure that your input files are correctly placed in the designated directories.

from Regex import *
from time import time

n = int((input("Enter the number of file pairs : ")))

try:
    programStart = time()
    for i in range(1, n + 1):
        patternFile = open(f'Inputs/Patterns/pattern{i}.txt', "r")
        textFile = open(f'Inputs/Texts/text{i}.txt', "r")
        outputFile = open(f'Outputs/patternmatch{i}.output', "w")

        pattern = patternFile.read().strip().lower()
        text = textFile.read().strip().lower()

        startTime = time()
        if '\\' in pattern:
            positionList = backslash_kmp_search(text, pattern)
        elif '.' in pattern:
            positionList = dot_kmp_search(text, pattern)
        elif '?' in pattern:
            positionList = question_kmp_search(text, pattern)
        elif '^' in pattern:
            positionList = startwith_kmp_search(text, pattern)
        elif '$' in pattern:
            positionList = endwith_kmp_search(text, pattern)
        else:
            positionList = kmp_search(text, pattern)
        endTime = time()

        if positionList:
            outputFile.write(str(len(positionList)) + " Match(es) Found!\n\n")
            for line, idx in positionList:
                outputFile.write("Line " + str(line) + ", Index " + str(idx) + "\n")
        else:
            outputFile.write("No Match Found!\n")

        outputFile.write(str(f"\nRuntime : {(endTime - startTime) * 1000 :.4f} milliseconds"))

        outputFile.close()
        textFile.close()
        patternFile.close()
    programEnd = time()

    print(f"\nAlgorithm Runtime : {(programEnd - programStart) * 1000 :.4f} milliseconds")
    print(f"You can find the results in Output Folder!")
except:
    print("Eror Occur!")
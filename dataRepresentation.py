import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter


def keywordCounter(fileToRead):
    # opens the file in read-only
    text_file = open(fileToRead, "r")
    # converts file into one string
    dataFromFile = text_file.read()
    # removes newline escapes from string
    strippedData = dataFromFile.rstrip('\n')
    # regex removes "[" and "]"
    dataWithoutBrackets = re.findall(r"\[(.*?)\]", strippedData)
    # Counter method iterates through strings and creates counter dict / obj
    objOfKeywords = Counter(dataWithoutBrackets)
    # close file
    text_file.close()
    return objOfKeywords






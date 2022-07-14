import os
import time


directoryToList = 'D:/temporary funnies/studio/posted/stuff to sell'
txtToWrite = 'D:/temporary funnies/text.txt'


def createTxt(targetDir, txtName):

    with open(txtName,'w') as file:
        for filename in os.scandir(targetDir):
            if filename.is_file():
                print(filename.stat())
                # file.write(filename.name[:-27])
                # file.write('\n')
                # file.write('\n')
        file.close()

# createTxt(directory, txtToWrite)

def fileSearchPrint(targetDir, arrayOfTags):
    for filename in os.scandir(targetDir):
        if filename.is_file():
            for tag in arrayOfTags:
                if tag in filename.name:
                    print(filename.name[:-27])



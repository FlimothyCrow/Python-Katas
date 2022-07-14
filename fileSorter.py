import os
import shutil


def createDirs(targetDirectory, arrayOfStrings):
    for dirString in arrayOfStrings:
        # loop through arrayOfStrings
        newDirectory = targetDirectory + "/" + dirString
        # append dirString onto targetDirectory
        if not os.path.exists(newDirectory):
            os.mkdir(newDirectory)
            # create directory if it doesn't already exist
            print("creating directory: " + newDirectory)
        else:
            print("SKIPPING {}".format(newDirectory))

def fileMatcher(targetString, substring):
    if substring in targetString:
        return True
    else:
        return False

def flattenDir(directory):
    for dirpath, _, filenames in os.walk(directory, topdown=False):
        for filename in filenames:
            i = 0
            source = os.path.join(dirpath, filename)
            target = os.path.join(directory, filename)
            while os.path.exists(target):
                i += 1
                file_parts = os.path.splitext(os.path.basename(filename))
                target = os.path.join(
                    directory,
                    file_parts[0] + "_" + str(i) + file_parts[1],
                )
            shutil.move(source, target)
            print("Moved ", source, " to ", target)
        if dirpath != directory:
            os.rmdir(dirpath)
            print("Deleted ", dirpath)

def fileMover(targetDir, listOfTerms):
    for term in listOfTerms:
        for element in os.listdir(targetDir):
            elementPath = targetDir + "/" + element
            if os.path.isfile(elementPath):
                # if element is a file
                if fileMatcher(element, term):
                    # if the filename contains the current term
                    print("moving " + element)
                    shutil.move(elementPath, str(targetDir + "/" + term))

def sorterController(targetDir, listOfTerms):
    flattenDir(targetDir)
    # recursively move all files into targetDir and delete folders
    createDirs(targetDir, listOfTerms)
    # create new folders based on search words array
    fileMover(targetDir, listOfTerms)
    # moves all matching files into new matching directories


directoryToPrint = 'C:/Users/Timothy/Desktop/TheCrow/target directory'
searchWords = ["ambush", "mummy", "cat's"]

sorterController(directoryToPrint, searchWords)
# TO DO map through files with regex to remove unnecessary punctuation from file names
# break file movement into separate function
# allow for files of same name


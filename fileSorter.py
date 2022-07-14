import os
import shutil
import re
import pathlib

def nameCleaner(strToClean):
    return re.sub(r'\W+', '', strToClean)

def createDirs(targetDir, arrayOfStrings):
    for dirString in arrayOfStrings:
        # loop through arrayOfStrings
        newDirectory = targetDir + "/" + dirString
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


def matchFinder(listOfFiles, listOfTerms):
    dictOfCounts = {}
    for term in listOfTerms:
        listOfMatches = []
        for file in listOfFiles:
            if fileMatcher(file, term):
                listOfMatches.append(file)
        # print("adding {} to dictOfCounts".format(term))
        dictOfCounts[term] = listOfMatches
    return dictOfCounts


def fileCopier(targetDir, dictOfCounts):
    for key in dictOfCounts.keys():
        for file in dictOfCounts[key]:
            filePath = str(targetDir + "/" + file)
            if os.path.isfile(filePath):
                print("copying: " + file)
                shutil.copy(filePath, str(targetDir + "/" + key))
    return targetDir


def fileDeleter(targetDir, dictOfCounts):
    # only deletes previously copied files, NOT unmatched files
    for key in dictOfCounts.keys():
        for file in dictOfCounts[key]:
            if os.path.isfile(str(targetDir + "/" + file)):
                print("deleting: " + file)
                os.remove(str(targetDir + "/" + file))
    return targetDir

def sorterController(targetDir, listOfTerms):
    flattenDir(targetDir)
    # recursively move all files into targetDir and delete folders
    createDirs(targetDir, listOfTerms)
    # create new folders based on search words array
    matchedFiles = matchFinder(os.listdir(targetDir), listOfTerms)
    # returns dictionary of {searchTerm: [arrayOfMatchingFilenames]}
    fileCopier(targetDir, matchedFiles)
    # copies all matching files into new matching directories
    fileDeleter(targetDir, matchedFiles)
    # deletes old matched copies of files from targetDir


targetDirectory = 'C:/Users/Timothy/Desktop/TheCrow/target directory'
searchWords = ["ambush", "mummy", "cat's"]

# sorterController(targetDirectory, searchWords)
# flattenDir(targetDirectory)

# TO DO map through files with regex to remove unnecessary punctuation from file names
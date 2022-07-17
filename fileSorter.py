import os
import shutil
import re
import timeit
import hashlib

def nameCleaner(strToClean):
    filename = os.path.splitext(strToClean)[0]
    extensionStr = os.path.splitext(strToClean)[1]
    return re.sub(r'\W+', '', filename).replace('_1', '') + extensionStr


def directorySanitizer(targetDir):
    # removes duplicate files and renames remaining files
    counter = 0
    unique = []
    files = os.listdir(targetDir)
    for file in files:
        # loop through all elements in directory
        filePath = targetDir + "/" + file
        if os.path.isfile(filePath):
            # if path is a file, clean its name string
            counter += 1
            filehash = md5(filePath)
            # get unique ID
            src = filePath
            dst = targetDir + "/" + nameCleaner(file)
            os.rename(src, dst)
            # rename with new cleaned string
            if filehash not in unique:
                unique.append(filehash)
            else:
                print("deleting " + filePath)
                os.remove(dst)
                # deletes matched duplicate using new cleaned string filepath


def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


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
    if substring.lower() in targetString.lower():
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
    count = 0
    for key in dictOfCounts.keys():
        for file in dictOfCounts[key]:
            filePath = str(targetDir + "/" + file)
            # filePath is defined BEFORE the file is copied
            if os.path.isfile(filePath):
                count += 1
                print("copying {}: ".format(count) + file)
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


def sorterController(targetDir, listOfTerms, flattenBoolean):
    start = timeit.default_timer()
    # start timer
    filteredListOfTerms = []
    [filteredListOfTerms.append(x) for x in listOfTerms if x not in filteredListOfTerms]
    # checking for duplicates in listOfTerms
    if flattenBoolean:
        flattenDir(targetDir)
    # recursively move all files into targetDir and delete folders
    # delete all checksum-identical files
    directorySanitizer(targetDir)
    # loops through flattened directory and runs each file through nameCleaner()
    createDirs(targetDir, filteredListOfTerms)
    # create new folders based on search words array
    matchedFiles = matchFinder(os.listdir(targetDir), filteredListOfTerms)
    # returns dictionary of {searchTerm: [arrayOfMatchingFilenames]}
    fileCopier(targetDir, matchedFiles)
    # copies all matching files into new matching directories
    fileDeleter(targetDir, matchedFiles)
    # deletes old matched copies of files from targetDir
    end = timeit.default_timer()
    # stop timer
    print("total time elapsed: " + str(end - start))
    print("directories created: " + str(len(filteredListOfTerms)))

targetDirectory = 'C:/Users/Timothy/Desktop/TheCrow/target directory'
searchWords = ["ambush", "mummy", "cat's", "mummy"]

# sorterController(targetDirectory, searchWords, True)

# flattenDir(targetDirectory)
# directorySanitizer(targetDirectory)
# md5(targetDirectory + "/" + "cat.png")
# removeDuplicates(targetDirectory)



# TO DO create new folders up one directory, or move them at the end
# TO DO directorySanitizer() and removeDuplicates() could be done in one loop
# what happens if I put "a multiple word string" in as a search term?
# total count of duplications created, unwanted duplicates removed
# undo button?
# BUG all copies are arriving with _1
# BUG program crashes sometimes on "file doesn't exist" errors

import os
import shutil
import re
import timeit
import hashlib

def nameCleaner(strToClean):
    filename = os.path.splitext(strToClean)[0]
    extensionStr = os.path.splitext(strToClean)[1]
    print("name cleaning " + filename)
    return re.sub(r'[^a-zA-Z0-9 \']+', '', filename).strip() + extensionStr


def directorySanitizer(targetDir):
    # removes duplicate files and renames remaining files
    unique = []
    files = os.listdir(targetDir)
    for file in files:
        # loop through all elements in directory
        filePath = targetDir + "/" + file
        if os.path.isfile(filePath):
            # if path is a file, clean its name string
            filehash = md5(filePath)
            # get unique ID
            src = filePath
            dst = targetDir + "/" + nameCleaner(file)
            os.rename(src, dst)
            # rename with new cleaned string
            if filehash not in unique:
                unique.append(filehash)
                print("validating " + file)
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


def flattenDir(srcDir, targetDir):
    for dirpath, _, filenames in os.walk(srcDir, topdown=False):
        for filename in filenames:
            i = 0
            source = os.path.join(dirpath, filename)
            target = os.path.join(targetDir, filename)
            while os.path.exists(target):
                i += 1
                file_parts = os.path.splitext(os.path.basename(filename))
                target = os.path.join(
                    targetDir,
                    file_parts[0] + "_" + str(i) + file_parts[1],
                )
            shutil.move(source, target)
            print("Moved ", source, " to ", target)
        if dirpath != srcDir:
            os.rmdir(dirpath)
            print("Deleted ", dirpath)


def matchFinder(listOfFiles, listOfTerms):
    dictOfCounts = {}
    for term in listOfTerms:
        listOfMatches = []
        for file in listOfFiles:
            print("checking " + str(file))
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


def sorterController(srcDirectory, targetDir, listOfTerms, sanitizeBoolean):
    # sC() can still be used to flatten and sanitize without listOfTerms
    start = timeit.default_timer()
    # start timer
    filteredListOfTerms = []
    flattenDir(srcDirectory, targetDir)
    # recursively move ALL files into targetDir and delete folders
    # delete all checksum-identical files

    if listOfTerms:
        [filteredListOfTerms.append(x) for x in listOfTerms if x not in filteredListOfTerms]
        # checking for duplicates in listOfTerms

    if sanitizeBoolean:
        directorySanitizer(targetDir)
        # loops through flattened directory
        # runs each file through nameCleaner()
        # runs each file through md5() and deletes duplicates

    if filteredListOfTerms:
        createDirs(targetDir, filteredListOfTerms)
        # create new folders based on search words array
        matchedFiles = matchFinder(os.listdir(targetDir), filteredListOfTerms)
        # returns dictionary of {searchTerm: [arrayOfMatchingFilenames]}
        fileCopier(targetDir, matchedFiles)
        # copies all matching files from targetDir into new matching directories
        fileDeleter(targetDir, matchedFiles)
        # deletes old matched copies of files from targetDir

    end = timeit.default_timer()
    # stop timer
    print("total time elapsed: " + str(end - start))
    if filteredListOfTerms:
        print("directories created: " + str(len(filteredListOfTerms)))

# INTEGRATION TEST BLOCK
#     targetDirectory = 'C:/Users/Timothy/Desktop/TheCrow/integration/target'
#     sourceDirectory = 'C:/Users/Timothy/Desktop/TheCrow/integration/source'
#     searchWords = ["ambush", "mummy", "cat's"]
#     sorterController(sourceDirectory, targetDirectory, searchWords, True, True)



src  = "example/directory0"
target = "example/directory1"
streamWords = ["example0", "example1"]
sorterController(src, target, streamWords, False)



# flattenDir(targetDirectory)
# directorySanitizer(targetDirectory)
# md5(targetDirectory + "/" + "cat.png")
# removeDuplicates(targetDirectory)

# to clean integration test directory:
    # open git bash
    # cd Desktop/TheCrow/integration
    # ./clean.sh

# BUG: some filenames are "too long"
# reconfigure loops in matchFinder
# files with / fail out, run sanitizer first
# what happens if I put "a multiple word string" in as a search term?
# what happens to files that are already in targetDir?
# total count of files moved, copied, duplicates found, renamed
# optional arguments: [list of words to delete file if matched], boolean to check for duplicates
# put totalFilesCount along with prints as "progress bar"

# refactor matchFinder() loop order as: (put time tester on this to show improvement)
    # for file in files:
        # for term in terms:
            # if term in file:
                # copy file to termDirectory

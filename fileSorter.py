import os
import shutil

# TO DO controller calls flattenDir()
# TO DO map through files with regex to remove unnecessary punctuation from file names
#
# controller calls createDirs() to loop through list of searchStrings and create a directory for each one (no dupes!)
# TO DO for each new directory, search the newly re-mapped targetDirectory for matches in filenames
# TO DO for each match, move that file to its new directory


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



# directoryToPrint = 'C:/Users/Timothy/Desktop/TheCrow/target directory'
# createDirs(directoryToPrint, ["ambush", "mummy", "things", "cat's"])
# directoryToFlatten = 'C:/Users/Timothy/Desktop/TheCrow/target directory/nostalgia'
# flattenDir(os.path.dirname(directoryToFlatten))

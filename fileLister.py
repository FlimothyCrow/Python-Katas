import os

directory = 'E:/music/study music'
# txtToWrite = 'D:/temporary funnies/list.txt'

def createTxt(targetDir, txtName):

    with open(txtName,'w') as file:
        for filename in os.scandir(targetDir):
            if filename.is_file():
                print(filename.name)
                file.write(filename.name)
                file.write('\n')
        file.close()

    # createTxt(directory, "study music.txt")

def fileSearch(targetDir, arrayOfTags):
    for filename in os.scandir(targetDir):
        if filename.is_file():
            for tag in arrayOfTags:
                if tag in filename.name:
                    print(filename.name[:-27])


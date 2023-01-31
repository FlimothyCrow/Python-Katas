from bs4 import BeautifulSoup
import requests
import re
from pathlib import Path


def returnAString(string) :
    return string


def recordingToDict(recording) :
    strippedPlayCount = int(re.sub(r'[^0-9]', '', recording.select_one('span.playCount').text))
    # removes all non-numerics, converts to int
    strippedDescription = recording.select_one('span.soundDescription').text.strip().replace('\n', '')
    # removes lead/trail whitespace and newlines
    sanitizedDescription = re.sub(r'[^A-Za-z0-9 ]+', '', strippedDescription)
    # removes nonalphanumeric, preserves whitespace

    recordingDict = {
        'link': recording.select_one('a').get("href"),
        'title': recording.select_one('a').text,
        'playCount': strippedPlayCount,
        'description': sanitizedDescription
    }
    return recordingDict


def getRecordings(url) :
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    recordings = soup.select('div.sound-details')

    listOfRecordingDicts = [recordingToDict(x) for x in recordings]

    return listOfRecordingDicts


def writeToFile():
    with open(f_path, 'w') as f:
        for recording in listOfParsedRecordings:
            f.write(f"{recording}\n")
            f.write(f"\n")

urlToRequest = "https://soundgasm.net/u/LonelyVA"

listOfParsedRecordings = getRecordings(urlToRequest)

f_path = Path(r"C:\Users\exampleDir\filename.txt")

# print(listOfParsedRecordings)
# writeToFile()

# things to do:
    # tighten up the stripping in recordingToDict()
    # add path argument to writeToFile()
    # add formatting to final file / convert to pdf?
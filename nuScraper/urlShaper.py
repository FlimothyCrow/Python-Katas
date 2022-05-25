
import pyperclip as pc
import time


def mockCase(string):
    new_quote = ""
    i = False
    for char in string:
        if i:
            new_quote += char.upper()
        else:
            new_quote += char.lower()
        if char != ' ':
            i = not i
    return new_quote


import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()

def objectCreator(arrayOfStrings):
    keys = ["url", "date", "priority"]
    # ["dummy URL", "dummy date", 0.80]
    dictionaryToReturn = {}
    for i in range(len(keys)):
        dictionaryToReturn[keys[i]] = arrayOfStrings[i]
    return dictionaryToReturn

def urlParser(urlString):
    # removes first 44 chars from URL
    # splits remaining string by "-" and returns array
    return urlString[44:].split("-")

def objectTagger(obj):
    # add "tags" key with urlParser(obj.url)
    # remove date and priority key/value pairs
    obj["tags"] = urlParser(obj["url"]) # ["string", "cheese", "cut", "fridge"]
    [obj.pop(key) for key in ["date", "priority"]]
    return obj

def controller(xmlFile):
    # takes root of xml file
    # each xml.node is parsed into object and pushed to array
    # {"url": "dummy URL", "date": "dummy date", "priority": 0.80}
    arrayOfNodeObjects = []

    for elem in xmlFile:
        arrayToParse = []
        for subelem in elem:
            arrayToParse.append(subelem.text)
        arrayOfNodeObjects.append(objectCreator(arrayToParse))
    result = map(objectTagger, arrayOfNodeObjects)
    for count, value in enumerate(list(result)):
        print(count, value)
        time.sleep(3)
        pc.copy(value["url"])

controller(root)

arrayOfUrls = ["https://hugelolcdn.com/i/829894.jpg", "https://hugelolcdn.com/i/830048.png", "https://hugelolcdn.com/i/829716.png"]

# it's iterating through a webscraper xml and copying all the urls to my downloader widget
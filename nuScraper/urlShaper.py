

import pyperclip as pc
import time
import re
import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()

def urlParser(urlString):
    # removes all chars up to final / (inclusive)
    # splits remaining string by "-" and returns array
    # . any given character
    #* iterator searching for . char type to match and consume (greedily, it stops at the final / )
    # / defines the stopping point
    # .* new character, iterating forward defined into a new group by ( )

    toReturn = re.compile('.*/(.*)')
    return toReturn.match(urlString).group(1).split("-")

def objectTagger(obj):
    # add "tags" key with urlParser(obj.url)
    # remove date and priority key/value pairs
    obj["tags"] = urlParser(obj["url"])
    return obj

def controller(xmlFile):
    # takes root of xml file as param
    arrayOfNodeObjects = []

    for elem in xmlFile:
        # each xml.node is parsed into object and pushed to array
        # {"url": "dummy URL"}
        objectToAppend = {"url": elem[0].text}
        arrayOfNodeObjects.append(objectToAppend)
    result = map(objectTagger, arrayOfNodeObjects)
    # map through array to split tags and define under "tags" key
    # {"url": "dummy URL", "tags": ["cheese", "eggs", "ham"]}
    for count, value in enumerate(list(result)):
        print(count, value)

        time.sleep(2)
        pc.copy(value["url"])
        # every two seconds, loop and copy url to clipboard

# controller(root)


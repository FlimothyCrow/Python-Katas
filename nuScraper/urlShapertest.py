
import unittest
from urlShaper import *


class scraper(unittest.TestCase):

    def test_mockCase(self):
        cased = mockCase("sandwich")
        self.assertEqual("sAnDwIcH", cased)

    def test_objectCreator(self):
        testingArray = ["dummy URL", "dummy date", 0.80]
        self.assertEqual({"url": "dummy URL", "date": "dummy date", "priority": 0.80}, objectCreator(testingArray))

    def test_urlParser(self):
        testString = "https://555555555.net/x/5151515151515851321/string-cheese-cut-fridge"
        self.assertEqual(["string", "cheese", "cut", "fridge"], urlParser(testString))

    def test_objectTagger(self):
        targetObject = {"url": "https://555555555.net/x/5151515151515851321/string-cheese-fridge", "date": "dummy date", "priority": 0.80}
        self.assertEqual({"url": "https://555555555.net/x/5151515151515851321/string-cheese-fridge", "tags": ["string", "cheese", "fridge"]}, objectTagger(targetObject))
import unittest
from fileSorter import *

class sorter(unittest.TestCase):

    def test_fileMatcher(self):
        self.assertEqual(True, fileMatcher("things", "gs"))
        self.assertEqual(True, fileMatcher("wordswendy's", "wendy's"))
        self.assertEqual(False, fileMatcher("things", "f"))

    def test_nameCleaner(self):
        self.assertEqual("things", nameCleaner("things///---*&%@#"))
        self.assertEqual("things.jpg", nameCleaner("things///---*&%@#.jpg"))

    def test_matchFinder(self):
        self.assertEqual({"cheese": ["cheese", "cheese55"]}, matchFinder(
            ["cheese", "cheese55"],
            ["cheese"]))


import unittest
from fileSorter import *

class sorter(unittest.TestCase):

    def test_fileMatcher(self):
        self.assertEqual(True, fileMatcher("things", "gs"))
        self.assertEqual(True, fileMatcher("things", "GS"))
        self.assertEqual(True, fileMatcher("wordswendy's", "wendy's"))
        self.assertEqual(False, fileMatcher("things", "f"))

    def test_nameCleaner(self):
        self.assertEqual("things.jpg", nameCleaner("things///---*&%@#_1_1.jpg"))
        self.assertEqual("cheese.jpeg", nameCleaner("cheese///---*&%@#_1_1.jpeg"))
        self.assertEqual("waffle.gif", nameCleaner("waffle///.---*&%@#_1_1.gif"))
        # self.assertEqual("eat at joe's.mp3", nameCleaner("eat at joe's %%#_1.mp3"))

    def test_matchFinder(self):
        self.assertEqual({"cheese": ["cheese", "cheese55"]}, matchFinder(
            ["cheese", "cheese55"],
            ["cheese"]))


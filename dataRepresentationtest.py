
import unittest
from dataRepresentation import *


class sandbox(unittest.TestCase):

    def test_keywordCounter(self):
        objOfKeywords = {
            "high": 1,
            "high voltage": 2,
            "cheese": 2,
            "life coach": 1,
            "things": 2,
            "stuff": 1,
            "word": 2
        }
        self.assertEqual(objOfKeywords, keywordCounter("smallKeywords.txt"))

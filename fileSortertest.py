import unittest
from fileSorter import *

class sorter(unittest.TestCase):

    def test_fileMatcher(self):
        self.assertEqual(True, fileMatcher("things", "gs"))
        self.assertEqual(False, fileMatcher("things", "f"))

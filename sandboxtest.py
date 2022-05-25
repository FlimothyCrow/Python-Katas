
import unittest
from sandbox import *


class sandbox(unittest.TestCase):

    def test_mockCase(self):
        cased = mockCase("sandwich")
        self.assertEqual("sAnDwIcH", cased)

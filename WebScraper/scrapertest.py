import unittest
from scraper import *

class MyTestCase(unittest.TestCase):
    def test_returnAString(self):
        self.assertEqual("cheesemas", returnAString("cheesemas"))


if __name__ == '__main__':
    unittest.main()

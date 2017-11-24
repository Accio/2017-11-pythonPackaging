import unittest
import myPyPkg

class TestPythagorean(unittest.TestCase):
    def test(self):
        self.assertEqual(myPyPkg.pythagorean(3,4), 5)

		

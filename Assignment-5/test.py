import unittest
import program

class UT(unittest.TestCase):
    def test_add(self):
        self.assertEqual(program.add(0,0),0)
        self.assertEqual(program.add(1,9),10)
        self.assertEqual(program.add(-4,0),-4)
        self.assertEqual(program.add(-3,-7),-10)
        # self.assertEqual(program.add(-3,-7),-1)
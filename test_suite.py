import unittest
import smars_library.smars_library as sl

class test_smarslab(unittest.TestCase):

    def test_create_robot(self):
        r = sl.SmarsRobot
        r.name = "test"
        self.assertTrue(r.name == "test")

if __name__ == '__main__':
    unittest.main()
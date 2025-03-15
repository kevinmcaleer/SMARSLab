import unittest
import smars_library.smars_library as sl

class test_smarslab(unittest.TestCase):

    def test_create_robot(self):
        robot = sl.SmarsRobot
        robot.name = "test"
        self.assertTrue(robot.name == "test")

if __name__ == '__main__':
    unittest.main()
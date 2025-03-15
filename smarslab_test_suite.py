# SMARSLab test suite

import unittest

from smars_library.smars_library import SmarsRobot  # Simplify/reduce redundancy


class SmarsLabTestCase(unittest.TestCase):
    """ tests SMARSLab  """

# TODO: add test cases
# TODO: check for website get 400
    pass


class CreateRobot(unittest.TestCase):

    def test_is_robot(self):
        robot = SmarsRobot()
        is_robot_instance = isinstance(robot, SmarsRobot)  # Clearer naming and separation
        self.assertIsInstance(robot, SmarsRobot, "Failed to create a valid SmarsRobot instance")


class TestSmarsRobot(unittest.TestCase):
    """Test case for the SmarsRobot class."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.robot = SmarsRobot()  # Initialize an instance of SmarsRobot to be tested

    def test_instance_creation(self):
        """Test that a SmarsRobot instance is created successfully."""
        self.assertIsInstance(self.robot, SmarsRobot, "Failed to create a valid SmarsRobot instance.")

    # Add other tests for behavior or properties if needed
    # def test_robot_behavior(self):
    #     self.assertTrue(self.robot.some_method(), "Behavior or method of SmarsRobot failed.")

    def test_name(self):
        self.robot.name = "test"
        self.assertTrue(self.robot.name == "test", "Failed to set name")

if __name__ == '__main__':
    unittest.main()

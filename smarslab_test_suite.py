# SMARSLab test suite

import unittest

import smars_lab
# from SMARS_Library3 import set_servo_pulse

class SmarsLabTestCase(unittest.TestCase):
    """ tests SMARSLab  """

# TODO: add test cases
# TODO: check for website get 400
    # def test_setServoPulseChannelLessThan15(self):
    #     for channel in range(0, 16):
    #         self.assertTrue(set_servo_pulse(channel, 10))

if __name__ == '__main__':
    unittest.main()

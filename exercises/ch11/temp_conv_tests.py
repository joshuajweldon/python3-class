import unittest
import temp_conv as tc


class TestConvTests(unittest.TestCase):

    def setUp(self):
        self.c_temperatures = (-40, 0, 100)
        self.f_temperatures = (-40, 32, 212)

    def testf2c(self):
        """test f2c function"""
        for c_temp, f_temp in zip(self.c_temperatures, self.f_temperatures):
            self.assertEqual(c_temp, tc.f2c(f_temp))

    def testc2f(self):
        """test c2f function"""
        for c_temp, f_temp in zip(self.c_temperatures, self.f_temperatures):
            self.assertEqual(f_temp, tc.c2f(c_temp))

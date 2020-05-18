import unittest
from circle import cir_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >=0, check if function works right
        self.assertAlmostEqual(cir_area(1), pi)
        self.assertAlmostEqual(cir_area(0), 0)
        self.assertAlmostEqual(cir_area(2.1), pi * 2.1**2)
        
    def test_values(self):
        # will find errors
        self.assertRaises(ValueError, cir_area, -2)
    def test_type(self):
        self.assertRaises(TypeError, cir_area, 3+5j)
        self.assertRaises(TypeError, cir_area, True)
        self.assertRaises(TypeError, cir_area, 'hey')
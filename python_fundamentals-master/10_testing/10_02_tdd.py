'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.


def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        return f"this won't work, {x} - {y} is 0 or lower."

        Check for correct results by providing an example input
Check that DivisionByZero errors get raised correctly
        '''
round
import yourpackage
import unittest


class TestYourPackage(unittest.TestCase):
    # define your tests as methods in here
    pass
    def test_yourtestmethodname(self):
    self.assertSOMETHING()
    def test_check_equality(self):
        """Expects the two inputs to be the same."""
        self.assertEquals(yourfunctioncall(arg1, arg2), expected_result)

    def test_raises_error(self):
        """Expects the defined error to be raised - e.g. here a ValueError."""
        with self.assertRaises(ValueError):
            your_function_call(arg1, arg2)
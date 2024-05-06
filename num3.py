import unittest
import sys
from datetime import datetime
import math

def factorial(n: int):
    if n < 0:
        raise ValueError("Error not found ^(")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Error")
    return result

class TestFactorial(unittest.TestCase):

    def testone(self):
        self.assertEqual(math.factorial(0), 1)

    def testtwo_pos(self):
        self.assertEqual(math.factorial(5), 120)

    def testthree_neg(self):
        with self.assertRaises(ValueError):
            math.factorial(-5)

    def testfourlarge(self):
        n = 100
        expected_log_factorial = math.lgamma(n + 1)
        actual_log_factorial = math.log(math.factorial(n))

        self.assertAlmostEqual(actual_log_factorial, expected_log_factorial, delta=1e-10)

    def testfivelargeinput(self):

        n = 3
        self.assertEqual(math.factorial(n), 	6)

if __name__ == "__main__":
    start_time = datetime.now()
    unittest.main()
    end_time = datetime.now()
    print(f"Время выполнения тестов: {end_time - start_time}")

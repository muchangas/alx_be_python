#!/usr/bin/env python3
# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
#!/usr/bin/env python3
"""
File: test_simple_calculator.py
Description: Unit tests for the SimpleCalculator class using the unittest module.
"""
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method."""
        # Create a fresh instance of the calculator for each test
        self.calc = SimpleCalculator()

    # --- Test Methods for add ---

    def test_addition_positive_numbers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(1, 99), 100)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-10, -5), -15)
        self.assertEqual(self.calc.add(-1, -99), -100)
        
    def test_addition_mixed_numbers(self):
        """Test addition with a mix of positive and negative numbers."""
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
        
    def test_addition_with_zero(self):
        """Test addition involving zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(-5, 0), -5)

    def test_addition_float_numbers(self):
        """Test addition with floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(-0.1, 0.2), 0.1)

    # --- Test Methods for subtract ---

    def test_subtraction_positive_numbers(self):
        """Test subtraction with two positive integers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative numbers (a - b)."""
        self.assertEqual(self.calc.subtract(-10, -5), -5) # -10 - (-5) = -5
        self.assertEqual(self.calc.subtract(-5, -10), 5)  # -5 - (-10) = 5

    def test_subtraction_with_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        
    def test_subtraction_float_numbers(self):
        """Test subtraction with floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(3.5, 1.2), 2.3)

    # --- Test Methods for multiply ---

    def test_multiplication_positive_numbers(self):
        """Test multiplication with two positive integers."""
        self.assertEqual(self.calc.multiply(10, 5), 50)
        
    def test_multiplication_negative_numbers(self):
        """Test multiplication with two negative integers."""
        self.assertEqual(self.calc.multiply(-10, -5), 50)

    def test_multiplication_mixed_numbers(self):
        """Test multiplication with a positive and a negative integer."""
        self.assertEqual(self.calc.multiply(-10, 5), -50)
        self.assertEqual(self.calc.multiply(10, -5), -50)

    def test_multiplication_with_zero(self):
        """Test multiplication involving zero."""
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        
    def test_multiplication_with_one(self):
        """Test multiplication involving one."""
        self.assertEqual(self.calc.multiply(10, 1), 10)

    # --- Test Methods for divide ---

    def test_division_normal(self):
        """Test division with positive integers resulting in a float."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_negative_result(self):
        """Test division resulting in a negative number."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(10, -5), -2.0)

    def test_division_by_zero(self):
        """Test the edge case of division by zero (should return None)."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Should also return None

    def test_division_zero_numerator(self):
        """Test division where the numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

    def test_division_float_numbers(self):
        """Test division with floating-point numbers."""
        # Use assertAlmostEqual for float comparisons
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

if __name__ == '__main__':
    # Running the tests directly
    unittest.main()
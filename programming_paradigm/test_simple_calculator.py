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
Description: Unit tests for the SimpleCalculator class.
"""
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class covering basic arithmetic 
    and edge cases like division by zero.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method."""
        # This ensures a fresh calculator instance for every test
        self.calc = SimpleCalculator()

    # --- Tests for add() ---

    
    def test_addition(self):
        """Test the addition method covering positive, negative, and mixed numbers."""
        
        # Test 1: Basic positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        
        # Test 2: Mixed signs resulting in zero
        self.assertEqual(self.calc.add(-1, 1), 0)
        
        # Test 3: Two negative numbers
        self.assertEqual(self.calc.add(-10, -5), -15)
        
        # Test 4: Floating-point numbers
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        
        # Test 5: Addition involving zero
        self.assertEqual(self.calc.add(0, 7), 7)
       
    # --- Tests for subtract() ---

        def test_subtraction(self)
            """Teat the subtraction of positive, negative, mixed and zero numbers"""
        # Test 1: Basic positive integers
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Test 2: Result is negative
        self.assertEqual(self.calc.subtract(4, 10), -6)
        
        # Test 3: Subtraction of two negative numbers
        self.assertEqual(self.calc.subtract(-5, -2), -3) # -5 - (-2) = -3
        
        # Test 4: Subtraction involving zero
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        
        # Test 5: Float subtraction
        self.assertAlmostEqual(self.calc.subtract(3.5, 1.2), 2.3)

    # --- Tests for multiply() ---

    def test_multiplication(self):
        """Test multiplication with positive integers."""
        self.assertEqual(self.calc.multiply(6, 7), 42)

        """Test multiplication with negative numbers and mixed signs."""
        self.assertEqual(self.calc.multiply(-5, 5), -25)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

        """Test multiplication involving zero (should always return 0)."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # --- Tests for divide() ---

    def test_division(self):
        """Test normal division resulting in an integer or float."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5)

        """Test division by zero, which should return None as per the function contract."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # 0/0 also returns None

        """Test division where the numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)

if __name__ == '__main__':
    # Allows running the tests directly
    unittest.main()
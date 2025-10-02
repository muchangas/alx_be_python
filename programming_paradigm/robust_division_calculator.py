#!/usr/bin/env python3
"""
File: robust_division_calculator.py
Description: Contains the safe_divide function for robust division with error handling.
"""

def safe_divide(numerator, denominator):
    """
    Performs division, robustly handling division by zero and non-numeric inputs.

    Args:
        numerator (str): The value for the numerator, passed as a string from command line.
        denominator (str): The value for the denominator, passed as a string from command line.

    Returns:
        str: A string containing the result or an appropriate error message.
    """
    try:
        # Step 1: Attempt to convert the string arguments to floating-point numbers
        num = float(numerator)
        den = float(denominator)

    except ValueError:
        # Catch if the conversion to float fails (e.g., 'ten' or 'abc')
        return "Error: Please enter numeric values only."

    try:
        # Step 2: Attempt the division operation
        result = num / den
        
        # Format the result to a reasonable number of decimal places for output
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Catch if the denominator is zero
        return "Error: Cannot divide by zero."
    
#!/usr/bin/env python3
"""
File: main.py
Description: Command-line interface for the robust division calculator.
"""
import sys
# Import the safe_divide function from the robust_division_calculator.py file
from robust_division_calculator import safe_divide

def main():
    """
    Main function to parse command-line arguments and display the result of safe_divide.
    """
    # Check if exactly 2 arguments (numerator and denominator) were provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are always strings when retrieved from sys.argv
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # The safe_divide function handles the type conversion and error checking
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()    
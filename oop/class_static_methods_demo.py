class Calculator:
    """
    A class demonstrating the use and differences between static methods
    and class methods in Python.
    """
    # Class Attribute: Accessible via the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method:
        Performs a calculation that doesn't rely on the class or instance state.
        It doesn't take 'self' or 'cls' as the first argument.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method:
        Performs a calculation and accesses a class attribute using the 'cls' parameter.
        It takes the class itself ('cls') as the first argument.
        """
        # Accessing the class attribute 'calculation_type' using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
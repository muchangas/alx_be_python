import math

# --- Base Class ---
class Shape:
    """
    Base class representing a generic shape.
    Defines the 'area' interface that must be implemented by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Raises NotImplementedError to enforce method overriding in derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")

# --- Derived Class: Rectangle (Method Overriding) ---
class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Overrides the area() method to calculate the rectangle's area.
    """
    def __init__(self, length, width):
        """Initializes a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width

# --- Derived Class: Circle (Method Overriding) ---
class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Overrides the area() method to calculate the circle's area.
    """
    def __init__(self, radius):
        """Initializes a Circle with a radius."""
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Formula: π * radius²
        """
        # Accesses math.pi from the imported math module
        return math.pi * (self.radius ** 2)

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
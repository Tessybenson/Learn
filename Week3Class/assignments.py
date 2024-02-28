from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Attempting to instantiate Shape directly will raise an error
# shape = Shape()  # This will raise an error

# Creating instances of concrete subclasses
rectangle = Rectangle(5, 4)
print("Area:", rectangle.area())  # Output: Area: 20
print("Perimeter:", rectangle.perimeter())  # Output: Perimeter: 18

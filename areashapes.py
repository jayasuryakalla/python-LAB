import math
class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses")
    def perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.base + self.side_a + self.side_b
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2 
    def perimeter(self):
        return 4 * self.side_length
def main():
    circle = Circle(radius=5)
    triangle = Triangle(base=4, height=3, side_a=5, side_b=6)
    square = Square(side_length=4)
    print("Circle:")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}\n")
    print("Triangle:")
    print(f"Area: {triangle.area():.2f}")
    print(f"Perimeter: {triangle.perimeter():.2f}\n")
    print("Square:")                        
    print(f"Area: {square.area():.2f}")
    print(f"Perimeter: {square.perimeter():.2f}")
if __name__ == "__main__":
     main()
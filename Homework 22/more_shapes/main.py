from shapes import Circle, Square, Rectangle
from shape_service import ShapeService

circle1 = Circle("red", "black", 5)
circle2 = Circle("blue", "green", 3)
print(circle1 == circle2)  # False

square1 = Square("yellow", "purple", 6)
square2 = Square("orange", "pink", 6)
print(square1 == square2)  # True

rectangle1 = Rectangle("blue", "green", 3, 4)
rectangle2 = Rectangle("red", "black", 2, 6)
print(rectangle1 == rectangle2)  # False

shapes = [circle1, circle2, square1, square2, rectangle1, rectangle2]
ShapeService.color_shapes(shapes, "white", "gray")
for shape in shapes:
    print(shape.get_inner_color(), shape.get_border_color())

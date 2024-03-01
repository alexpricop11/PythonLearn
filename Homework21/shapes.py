class Shape:
    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color

    def get_inner_color(self):
        return self._inner_color

    def set_inner_color(self, inner_color):
        self._inner_color = inner_color

    def get_border_color(self):
        return self._border_color

    def set_border_color(self, border_color):
        self._border_color = border_color


class Circle(Shape):
    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def _set_radius(self, radius):
        self._radius = radius


class Rectangle(Shape):
    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        self._length = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length
        self._width = length


class Square(Rectangle):
    def __init__(self, inner_color, border_color, side_length):
        super().__init__(inner_color, border_color, side_length, side_length)

    def set_width(self, width):
        super().set_width(width)
        super().set_length(width)

    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)


circle = Circle("red", "black", 5)
print("Circle Radius:", circle.get_radius())

rectangle = Rectangle("blue", "green", 3, 4)
print("Rectangle Width:", rectangle.get_width())
print("Rectangle Length:", rectangle.get_length())

square = Square("yellow", "purple", 6)
print("Square Width:", square.get_width())
print("Square Length:", square.get_length())

square.set_length(8)
print("Updated Square Width:", square.get_width())
print("Updated Square Length:", square.get_length())

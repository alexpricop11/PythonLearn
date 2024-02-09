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

    @property
    def area(self):
        raise NotImplementedError("Area calculation not implemented for Shape class")

    def __eq__(self, other):
        return type(self) is type(other)

    def __add__(self, other):
        if type(self) is type(other):
            raise NotImplementedError("Addition not implemented for this type of shape")
        else:
            raise TypeError("Shapes with different types cannot be added")

    def __sub__(self, other):
        if type(self) is type(other):
            raise NotImplementedError("Subtraction not implemented for this type of shape")
        else:
            raise TypeError("Shapes with different types cannot be subtracted")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            raise NotImplementedError("Multiplication not implemented for this type of shape")
        else:
            raise TypeError("Shapes can only be multiplied by a number")


class Circle(Shape):
    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def _set_radius(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.get_radius() == other.get_radius()
        return False

    def __add__(self, other):
        if isinstance(other, Circle):
            raise TypeError("Shapes with different types cannot be added")
        else:
            raise TypeError("Shapes with different types cannot be added")

    def __sub__(self, other):
        if isinstance(other, Circle):
            raise TypeError("Shapes with different types cannot be subtracted")
        else:
            raise TypeError("Shapes with different types cannot be subtracted")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            raise TypeError("Shapes can only be multiplied by a number")
        else:
            raise TypeError("Shapes can only be multiplied by a number")


class Rectangle(Shape):
    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    @property
    def area(self):
        return self._width * self._length

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            raise TypeError("Shapes with different types cannot be added")
        else:
            raise TypeError("Shapes with different types cannot be added")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            raise TypeError("Shapes with different types cannot be subtracted")
        else:
            raise TypeError("Shapes with different types cannot be subtracted")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            raise TypeError("Shapes can only be multiplied by a number")
        else:
            raise TypeError("Shapes can only be multiplied by a number")


class Square(Rectangle):
    def __init__(self, inner_color, border_color, side_length):
        super().__init__(inner_color, border_color, side_length, side_length)

    def set_width(self, width):
        super().set_width(width)
        super().set_length(width)

    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.get_width() == other.get_width()
        return False

    def __add__(self, other):
        if isinstance(other, Square):
            raise TypeError("Shapes with different types cannot be added")
        else:
            raise TypeError("Shapes with different types cannot be added")

    def __sub__(self, other):
        if isinstance(other, Square):
            raise TypeError("Shapes with different types cannot be subtracted")
        else:
            raise TypeError("Shapes with different types cannot be subtracted")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            raise TypeError("Shapes can only be multiplied by a number")
        else:
            raise TypeError("Shapes can only be multiplied by a number")
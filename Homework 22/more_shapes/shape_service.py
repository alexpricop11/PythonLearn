from shapes import Circle, Rectangle, Square


class ShapeService:
    DEFAULT_INNER_COLOR = "default_inner_color"
    DEFAULT_OUTER_COLOR = "default_outer_color"

    @staticmethod
    def create_default_circle(radius):
        return Circle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_OUTER_COLOR, radius)

    @staticmethod
    def create_default_rectangle(width, length):
        return Rectangle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_OUTER_COLOR, width, length)

    @staticmethod
    def create_default_square(side_length):
        return Square(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_OUTER_COLOR, side_length)

    @staticmethod
    def color_shapes(list_of_shapes, inner_color, border_color):
        for shape_instance in list_of_shapes:
            shape_instance.set_inner_color(inner_color)
            shape_instance.set_border_color(border_color)

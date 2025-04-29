from modules import demo

NUMBER_OF_SHAPES = 500000


def compute_total_area():
    shapes = create_shapes()
    return sum(shape.area() for shape in shapes)


def create_shapes():
    shapes = []
    for i in range(NUMBER_OF_SHAPES):
        if i % 2 == 0:
            shapes.append(demo.Circle(i % 100 + 1))
        else:
            shapes.append(demo.Square(i % 100 + 1))
    return shapes

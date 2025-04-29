from modules import demo
from modules import clean

NUMBER_OF_SHAPES = 500000


def compute_total_area(module_name):
    shapes = create_shapes(module_name)
    return sum(shape.area() for shape in shapes)


def create_clean_shapes():
    shapes = []
    for i in range(NUMBER_OF_SHAPES):
        if i % 2 == 0:
            shapes.append(clean.Circle(i % 100 + 1))
        else:
            shapes.append(clean.Square(i % 100 + 1))
        return shapes


def create_optimized_shapes():
    shapes = []
    for i in range(NUMBER_OF_SHAPES):
        if i % 2 == 0:
            shapes.append(clean.Circle(i % 100 + 1))
        else:
            shapes.append(clean.Square(i % 100 + 1))
    return shapes


def create_shapes(module_name):
    if module_name == "clean":
        shapes = create_clean_shapes()
    else:
        shapes = create_optimized_shapes()
    return shapes

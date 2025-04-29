from modules import demo
from modules import clean
from modules import wrapper

NUMBER_OF_SHAPES = 500000


def compute_total_area(module_name):
    shapes = create_shapes(module_name)
    return sum(shape.area() for shape in shapes)


def side_from_index(index):
    return index % 100 + 1


def create_shapes(module_name):
    shapes = []
    w = wrapper.Wrapper(module_name)
    for i in range(NUMBER_OF_SHAPES):
        if i % 2 == 0:
            shapes.append(w.Circle(side_from_index(i)))
        else:
            shapes.append(w.Square(side_from_index(i)))
    return shapes

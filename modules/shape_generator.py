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
    shapes = Shapes(module_name)
    shape_wrapper = wrapper.Wrapper(module_name)
    j = 0
    for i in range(NUMBER_OF_SHAPES):
        if j == 0:
            shapes.shape_list.append(shape_wrapper.Circle(side_from_index(i)))
        elif j == 1:
            shapes.shape_list.append(shape_wrapper.Square(side_from_index(i)))
        j += 1
        j %= 2
    return shapes.shape_list


class Shapes:
    def __init__(self, module_name):
        self.wrapper = wrapper.Wrapper(module_name)
        self.shape_list = []

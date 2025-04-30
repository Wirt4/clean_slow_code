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
    for i in range(NUMBER_OF_SHAPES):
        shapes.append_next_shape(i)
    return shapes.shape_list


class Shapes:
    def __init__(self, module_name):
        self.wrapper = wrapper.Wrapper(module_name)
        self.shape_list = []
        self.modulus_index = 0

    def append_next_shape(self, index):
        if self.modulus_index == 0:
            self.shape_list.append(self.wrapper.Circle(side_from_index(index)))
        elif self.modulus_index == 1:
            self.shape_list.append(self.wrapper.Square(side_from_index(index)))
        self.modulus_index += 1
        self.modulus_index %= 2

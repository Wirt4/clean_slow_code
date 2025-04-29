from modules import demo


def compute_total_area():
    shapes = create_shapes()
    return sum(shape.area() for shape in shapes)


def create_shapes():
    shapes = []
    number_of_shapes = 500000
    for i in range(number_of_shapes):
        if i % 2 == 0:
            shapes.append(demo.Circle(i % 100 + 1))
        else:
            shapes.append(demo.Square(i % 100 + 1))
    return shapes

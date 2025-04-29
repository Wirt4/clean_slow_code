from modules import demo


def compute_total_area():
    shapes = create_shapes()
    return sum(shape.area() for shape in shapes)
    total = 0.0
    for shape in shapes:
        total += shape.area()
    return total


def create_shapes():
    shapes = []
    for i in range(500000):
        if i % 2 == 0:
            shapes.append(demo.Circle(i % 100 + 1))
        else:
            shapes.append(demo.Square(i % 100 + 1))
    return shapes

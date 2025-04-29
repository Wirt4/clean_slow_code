import math


class Shape:
    def area(self):
        raise NotImplementedError()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def compute_total_area(shapes):
    total = 0.0
    for shape in shapes:
        total += shape.area()
    return total


def create_shapes():
    shapes = []
    for i in range(500000):
        if i % 2 == 0:
            shapes.append(Circle(i % 100 + 1))
        else:
            shapes.append(Square(i % 100 + 1))
    return shapes


def main():
    shapes = create_shapes()
    total = compute_total_area(shapes)
    print(f"Total area: {total}")


if __name__ == "__main__":
    main()

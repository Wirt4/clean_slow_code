from modules import random_shapes
from modules.oop import total_area_oop, Shape
from modules.struct import total_area_struct, ShapeStruct


class ProfileFunctions:
    shape_list_size: int = 100000

    @staticmethod
    def run_oop() -> None:
        shapes: list[Shape] = ProfileFunctions.make_list(random_shapes.random_shape_oop)
        total_area_oop(shapes)

    @staticmethod
    def run_struct() -> None:
        shapes: list[ShapeStruct] = ProfileFunctions.make_list(
            random_shapes.random_shape_struct
        )
        total_area_struct(shapes)

    @staticmethod
    def make_list(shape_lambda):
        return [shape_lambda() for _ in range(ProfileFunctions.shape_list_size)]

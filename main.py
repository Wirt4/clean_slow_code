import cProfile
from modules import shape_generator

cProfile.run("shape_generator.compute_total_area()")

import cProfile
from modules import demo

cProfile.run("demo.compute_total_area(demo.create_shapes())")

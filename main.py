import cProfile
from modules import shape_generator

print("profiling clean code version")
cProfile.run("shape_generator.compute_total_area()")
print("profling optimized version")
cProfile.run("shape_generator.compute_total_area()")

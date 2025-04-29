import cProfile
import sys
from modules import shape_generator

module_name = sys.argv[1]
print("module name is", module_name)

print("profiling demo version")
cProfile.run("shape_generator.compute_total_area('demo')")
print("profling clean version")
cProfile.run("shape_generator.compute_total_area('clean')")

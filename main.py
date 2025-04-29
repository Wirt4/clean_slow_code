import cProfile
import sys
from modules import shape_generator

module_name = sys.argv[1]
print("profiling", module_name)
cProfile.run("shape_generator.compute_total_area('{}')".format(module_name))

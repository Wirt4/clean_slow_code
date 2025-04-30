import cProfile
from modules import clean

print("profiling clean example")
cProfile.run("clean.compute_total_area_polymorphism(0,[])")

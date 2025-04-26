import timeit

setup_code = """
from clean import create_shapes, compute_total_area
shapes = create_shapes()
"""

stmt_code = "compute_total_area(shapes)"

# timeit: run 1 iteration (number=1), repeated 3 times (repeat=3)
time_taken = timeit.timeit(stmt=stmt_code, setup=setup_code, number=1)
print(f"OOP version took {time_taken:.4f} seconds")

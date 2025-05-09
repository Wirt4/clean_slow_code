import cProfile

from modules.profile_methods import run_oop, run_typeddict

"""
Main entry ProfileFunctions
runs the profiles for the clean object-oriented functions and for the "dirty" old fashioned TypedDict functions
"""
if __name__ == "__main__":
    run_typeddict()
    run_oop()
    print("TypedDict Version:")
    cProfile.run("run_typeddict()", sort="cumulative")
    print("OOP Version:")
    cProfile.run("run_oop()", sort="cumulative")

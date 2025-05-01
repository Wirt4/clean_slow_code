import cProfile
from modules.profile_methods import run_oop, run_struct

"""
Main entry ProfileFunctions
runs the profiles for the clean object-oriented functions and for the "dirty" old fashioned struct functions
"""
if __name__ == "__main__":
    print("OOP Version:")
    cProfile.run("run_oop()", sort="cumtime")

    print("\nFlat Struct Version:")
    cProfile.run("run_struct()", sort="cumtime")

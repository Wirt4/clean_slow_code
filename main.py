import cProfile
from modules import profile_methods

"""
Main entry ProfileFunctions
runs the profiles for the clean object-oriented functions and for the "dirty" old fashioned struct functions
"""
if __name__ == "__main__":
    print("OOP Version:")
    cProfile.run("profile_methods.ProfileFunctions.run_oop()", sort="cumtime")

    print("\nFlat Struct Version:")
    cProfile.run("profile_methods.ProfileFunctions.run_struct()", sort="cumtime")

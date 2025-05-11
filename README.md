# clean_slow_code

## Hypothesis
Structuring operations based on lookup tables and switch-like blocks will be 2 to 10 times as performant as structuring the code with class methods and polymorphism. This is based on the demo and article at <https://www.computerenhance.com/p/clean-code-horrible-performance>

Casey Muratori's C++ demonstration claims a 10x speed improvement when ditching polymorphism and other 'Clean Code' practices. If polymorphism or Clean Code are inherently poor concepts, then there should be a similar(if not as dramatic) difference in benchmark performance when applied to a different language, even a high-level scripting language like Python.

## Procedure
There are two scripts:`class_hiearcy.py` and `struct_like.py`. Each reads a list of shape types and dimensions, calculates the sum of the total area, and the sum of the total corner weighted area.

    if __name__ == "__main__":
        # read the list of shapes
        shapes: list[ShapeBase] = read_profiles_to_shapes("shapes.txt")
        total_area(shapes)
        total_corner_weighted_area(shapes)


    if __name__ == "__main__":
        # read the list of shapes
        shapes: list[ShapeUnion] = read_profiles_to_shapes("shapes.txt")
        total_area(shapes)
        total_corner_weighted_area(shapes)

CProfile is used to get the stats of each script separately. A BASH script is used to run the script and open the profile in the terminal browser to streamline the process.

example:`sh profile.sh class_hiearchy`

To make sure each script is runs the same data set, they both read from the same file, "shapes.txt". I'ts part of .gitignore to avoid large file sizes. The python script `generate_shapes.py` takes a command line argument and creates a text file of randomized shape types and dimensions for each implementation to read.

    square 9.021502147952276
    triangle 8.497971160725204 2.197869451840505
    circle 1.1520596632968783
    triangle 3.21495952717547 9.052872450488561
    triangle 2.5521488886475163 6.682753930489702
    square 2.0220271390156324

`generate_shapes.py` takes a command-line argument to specify the number to generate. I used 1,000,000 for this example.

    generate_shapes.py 1000000

File reading adds a little overhead, but it's a straightforward way to set up the comparision.

class hiearchy:

    def read_profiles_to_shapes(filename: str) -> list[ShapeBase]:
        shapes: list[ShapeBase] = []
        with open(filename, "r") as f:
            for line in f:
                shapes.append(shape_factory(line.strip().split()))
        return shapes


struct-like:

    def read_profiles_to_shapes(filename: str) -> list[ShapeUnion]:
        shapes: list[ShapeUnion] = []
        with open(filename, "r") as f:
            for line in f:
                shapes.append(specs_to_shape(line.strip().split()))
        return shapes

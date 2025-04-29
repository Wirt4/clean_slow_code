import os
import sys


## script structure
class CommandWrapper:
    def __init__(self, timeit_args):
        self.timeit_args = timeit_args

    def run(self):
        self._print_alert()
        self._execute(self._parse_command())

    def _print_alert(self):
        print("Running benchmark for {}.py ...".format(self.timeit_args.source))

    def _execute(self, command):
        os.system(command)

    def _parse_command(self):
        return "python3 -m {}".format(self._timeit(self.timeit_args))

    def _timeit(self, args):
        return "timeit -n {} -r {} -s {}".format(
            args.times_to_run, args.repeats, args.statement
        )


class TimeItArguments:
    def __init__(self, source, times_to_run, repeats=1):
        self.source = source
        self.times_to_run = times_to_run
        self.repeats = repeats
        self.statement = '"from {} import {}"'.format(source, Imports())


class Imports:
    def __init__(self):
        self._imports = ["create_shapes", "compute_total_area"]

        self._commands = ["shapes = create_shapes()", "compute_total_area(shapes)"]

    def __str__(self):
        return "{}; {}".format(self.imports(), self.commands())

    def imports(self):
        return ", ".join(self._imports)

    def commands(self):
        return '" "'.join(self._commands)


## execution
argument = sys.argv[1]
default_times_to_run = 100
if len(sys.argv) > 2:
    times_to_run = int(sys.argv[2])
else:
    times_to_run = default_times_to_run

timeItArgs = TimeItArguments(argument, times_to_run)
command = CommandWrapper(timeItArgs)
command.run()

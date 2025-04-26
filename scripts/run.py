import os
import sys

class CommandWrapper:
    def __init__(self, command):
        self.command = command

    def run(self):
        self._print_alert()
        self._execute(self._parsed_command())

    def _print_alert(self):
        print("Running benchmark for {}.py ...".format(self.command))
    
    def _execute(self, command):
        os.system(command)

    def _parsed_command(self):
        run_python= 'python3 -m'
        imports = ['create_shapes', 'compute_total_area']
        python_commands= ['shapes = create_shapes()', 'compute_total_area(shapes)']
        import_statement = '"from {} import {}; {}"'.format(self.command, ', '.join(imports),'" "'.join(python_commands))
        times_to_run = 100
        timeit = 'timeit -n {} -r 1  -s {}'.format(times_to_run, import_statement) 
        return '{} {}'.format(run_python, timeit)
    
argument = sys.argv[1]
command = CommandWrapper(argument)
command.run()
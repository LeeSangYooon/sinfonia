from parser.Parser import parse
from parser.ProgramParser import ProgramParser
from parse_tree_generator.ParseTreeGenerator import generate_parse_tree, AST
from machine_code_generator.MachineCode import MachineCode
from machine_code_generator.MachineCodeGenerator import generate_machine_code
import virtual_machine.VirtualMachine as VM
from utility.Timer import timer
import time
from sys import argv
import os


if __name__ == "__main__":
    file_path = argv[1]
    file = open(file_path, mode="r").read()
    directory = os.path.dirname(file_path)

    # Get the file name (without the directory path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Generate the file path for the machine code file
    machine_code_file_path = os.path.join(directory, f"{file_name}.svmc")


    tree, parser = timer('parsing', lambda:parse(file))
    ast: AST.ProgramNode = timer('semantic analyzing', lambda: generate_parse_tree(tree))
    machine_code: MachineCode = timer('generating machine code', lambda: generate_machine_code(ast))

    # Write the machine code to the generated file path
    with open(machine_code_file_path, "w") as file:
        file.write(machine_code.save_format())
        time.sleep(1)
        print('Compiled Successfully on', machine_code_file_path)
    

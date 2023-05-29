from parser.Parser import parse
from parser.ProgramParser import ProgramParser
from semantic_analyizer.SemanticAnalyizer import semantic_analyze, AST
from machine_code_generator.MachineCode import MachineCode
from machine_code_generator.MachineCodeGenerator import generate_machine_code
import virtual_machine.VirtualMachine as VM
from utility.Timer import timer




if __name__ == "__main__":
    file = open('test_codes/test_code.sfn', mode="r").read()
    tree, parser = parse(file)
    ast: AST.ProgramNode = semantic_analyze(tree)
    machine_code: MachineCode = generate_machine_code(ast)
    print(machine_code)
    vm = VM.VirtualMachine()
    vm.run(machine_code)

#print(tree.toStringTree(recog=parser))

"""
vm = VM.VirtualMachine()
print(multiply_machine_code)
#vm.run(multiply_machine_code)

print("break")
"""
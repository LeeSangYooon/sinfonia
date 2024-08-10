from sys import argv
from machine_code_generator.MachineCode import MachineCode
from virtual_machine.VirtualMachine import VirtualMachine

if __name__ == "__main__":
    file_path = argv[1]
    file = open(file_path, mode="r").read()
    machine_code = MachineCode()
    machine_code.open_format(file)
    vm = VirtualMachine()
    vm.run(machine_code)
    

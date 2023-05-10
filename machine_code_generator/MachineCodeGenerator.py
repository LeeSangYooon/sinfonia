from semantic_analyizer.AST.AST import ASTNode
import semantic_analyizer.AST.ASTNodes as AST
from .MachineCode import MachineCode

def generate_machine_code(ast: AST.ProgramNode) -> MachineCode:
    machine_code = MachineCode()
    return machine_code
from .AST import ASTNode
from typing import List
from .StatementNodes import *
from .ExprNodes import *

class FirstNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()

class ProgramNode(ASTNode):
    def __init__(self, first_nodes: List[FirstNode]) -> None:
        self.first_nodes: List[FirstNode] = first_nodes
        super().__init__()


class FuncTypeNode(ASTNode):
    def __init__(self, input_types: List[str], output_type: str) -> None:
        self.input_types: List[str] = input_types
        self.output_type: str = output_type
        super().__init__()





class FuncDeclNode(FirstNode):
    def __init__(self, func_type: FuncTypeNode, block: BlockNode) -> None:
        self.func_type: FuncTypeNode = func_type
        self.block: BlockNode = block
        super().__init__()
    

class VarDeclNode(ASTNode):
    def __init__(self, type_name:str, var_name:str, expr:ExprNode = None ) -> None:
        self.type_name = type_name
        self.var_name = var_name
        self.expr = expr
        super().__init__()

class ClassDeclNode(FirstNode):
    def __init__(self,name:str, funcs: List[FuncDeclNode], vars: List[VarDeclNode]) -> None:
        self.name= name
        self.funcs = funcs
        self.vars = vars
        super().__init__()



from .AST import ASTNode
from typing import List

class FirstNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()

class ProgramNode(ASTNode):
    def __init__(self, first_nodes: List[FirstNode]) -> None:
        self.first_nodes: List[FirstNode] = first_nodes
        super().__init__()



class FuncDeclNode(FirstNode):
    def __init__(self) -> None:
        super().__init__()

class VarDeclNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()

class ClassDeclNode(FirstNode):
    def __init__(self, funcs: List[FuncDeclNode], vars: List[VarDeclNode]) -> None:
        self.funcs = funcs
        self.vars = vars
        super().__init__()

class StatementNode(FirstNode):
    def __init__(self) -> None:
        super().__init__()


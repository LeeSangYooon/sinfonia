from .AST import ASTNode
from .ExprNodes import ExprNode
from typing import List

class StatementNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()

class BlockNode(ASTNode):
    def __init__(self, statements: List[StatementNode]) -> None:
        self.statements = statements
        super().__init__()

class IfStatNode(StatementNode):
    def __init__(self, expr: ExprNode, block: BlockNode) -> None:
        self.expr =expr
        self.block = block
        super().__init__()  


class ForStatNode(StatementNode):
    def __init__(self, counter_expr: ExprNode, expr: ExprNode, block: BlockNode) -> None:
        self.counter_expr = counter_expr
        self.expr = expr
        self.block = block
        super().__init__()

class WhileStatNode(StatementNode):
    def __init__(self, condition_expr: ExprNode, block: BlockNode) -> None:
        self.condition_expr = condition_expr
        self.block = block
        super().__init__()


class SetStatNode(StatementNode):
    def __init__(self, left, right: ExprNode) -> None:
        self.left = left
        self.right = right
        super().__init__()

class FuncCallNode(StatementNode):
    def __init__(self, func_name, inputs:List[ExprNode]) -> None:
        self.func_name = func_name
        self.inputs = inputs
        super().__init__()
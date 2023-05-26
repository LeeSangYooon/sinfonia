from .AST import ASTNode
from typing import List



class AtomNode(ASTNode):
    def __init__(self) -> None:
        
        super().__init__()

class LiteralNode(AtomNode):
    def __init__(self) -> None:
        super().__init__()

class IntLiteralNode(LiteralNode):
    def __init__(self, number: int) -> None:
        self.number = number
        super().__init__()

class StrLiteralNode(LiteralNode):
    def __init__(self, string: str) -> None:
        self.string = string
        super().__init__()

class ClassObjectNode(AtomNode):
    def __init__(self, sequence: List[str]) -> None:
        self.sequence = sequence
        super().__init__()



class MultExprNode(ASTNode):
    def __init__(self, atoms: AtomNode, operators: List[str]) -> None:
        self.atoms = atoms
        self.operators = operators
        super().__init__()

class ExprNode(ASTNode):
    def __init__(self, mult_expr_nodes: List[MultExprNode], operators: List[str]) -> None:
        self.mult_expr_nodes = mult_expr_nodes
        self.operators = operators
        super().__init__()

class ComparisonNode(AtomNode):
    def __init__(self, operator: str, left_expr:ExprNode, right_expr:ExprNode) -> None:
        self.operator = operator
        self.left_expr = left_expr
        self.right_expr = right_expr
        super().__init__()
    
class FactorNode(AtomNode):
    def __init__(self, comparison: ComparisonNode = None, condition = None) -> None:
        self.comparison = comparison
        self.condition = condition
        super().__init__()


# AND operations
class TermNode(AtomNode):
    def __init__(self, factors: List[FactorNode]) -> None:
        self.factors = factors
        super().__init__()

# OR operations
class ConditionNode(AtomNode):
    def __init__(self, terms: List[TermNode]) -> None:
        self.terms = terms
        super().__init__()


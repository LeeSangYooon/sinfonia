from .AST import ASTNode

class StatementNode(ASTNode):
    def __init__(self) -> None:
        super().__init__()

class IfStatNode(StatementNode):
    def __init__(self) -> None:
        super().__init__()  


class ForStatNode(StatementNode):
    def __init__(self) -> None:
        super().__init__()

class WhileStatNode(StatementNode):
    def __init__(self) -> None:
        super().__init__()


class SetStatNode(StatementNode):
    def __init__(self) -> None:
        super().__init__()

class FuncCallNode(StatementNode):
    def __init__(self) -> None:
        super().__init__()
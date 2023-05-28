from parser.ProgramParser import ProgramParser as Parser
from .AST.AST import ASTNode
import semantic_analyizer.AST.ASTNodes as AST
from typing import List
from antlr4.tree.Tree import TerminalNode, TerminalNodeImpl
from machine_code_generator.SymbolTable.Type import Type

def semantic_analyze(root_node: Parser.ProgContext) -> AST.ProgramNode:
    first_nodes:List[Parser.FirstContext] = []
    for first in root_node.first():
        first: Parser.FirstContext
        first_node: AST.FirstNode

        if first.class_decl():
            first_node = class_decl_ast(first.class_decl())

        if first.func_decl():
            first_node = func_decl_ast(first.func_decl())

        if first.statement():
            first_node = statement_ast(first.statement())
        
        first_nodes.append(first_node)
    program_node = AST.ProgramNode(first_nodes=first_nodes)
    return program_node

def block_ast(block_node: Parser.BlockContext) -> AST.BlockNode:
    statements: List[AST.StatementNode] = []
    
    for statement in block_node.statement():
        statement: Parser.StatementContext
        statements.append(statement_ast(statement))
    
    return AST.BlockNode(statements=statements)

def class_decl_ast(class_decl_node: Parser.Class_declContext) -> AST.ClassDeclNode:
    func_decls: List[AST.FuncDeclNode] = []
    class_var_decls: List[AST.VarDeclNode] = []
    name: str

    if class_decl_node.func_decl():
        for func_decl_node in class_decl_node.func_decl():
            func_decl_node: Parser.Func_declContext
            func_decls.append(func_decl_ast(func_decl_node))
        
    if class_decl_node.class_var_decl():
        for var_decl_node in class_decl_node.class_var_decl():
            var_decl_node: Parser.Var_declContext
            class_var_decls.append(var_decl_ast(var_decl_node=var_decl_node, class_var=True))

    name = class_decl_node.ID().getText()

    class_decl_node_ast = AST.ClassDeclNode(name= name,funcs=func_decls, vars=class_var_decls)
    return class_decl_node_ast

def func_decl_ast(func_decl_node: Parser.Func_declContext) -> AST.FuncDeclNode:
    # function type
    type_node: Parser.Func_typeContext = func_decl_node.func_type()
    types: List[TerminalNodeImpl] = type_node.ID()
    *input_types, output_type = list(map(lambda x: Type(x.getText()), types))
    func_type_node_ast = AST.FuncTypeNode(input_types=input_types, output_type=output_type)
    #print(input_types, output_type)
    #func_name
    head: Parser.Func_headContext = func_decl_node.func_head()
    name, *args = map(str, head.ID())
    # function body
    block_node = block_ast(func_decl_node.block())
    func_decl_node_ast = AST.FuncDeclNode(func_type=func_type_node_ast, block=block_node, name=name, args= args)
    return func_decl_node_ast


def var_decl_ast(var_decl_node: Parser.Var_declContext | Parser.Class_var_declContext, class_var = False) -> AST.VarDeclNode:
    if class_var:
        var_decl_node: Parser.Class_var_declContext
    else:
        var_decl_node: Parser.Var_declContext
    
    type_name, var_name, *rest  = list(map(lambda x: x.getText(), var_decl_node.ID()))
    type_name = Type(type_name)
    
    if not class_var:
        expr_node = expr_ast(var_decl_node.expr())
        var_decl_node_ast = AST.VarDeclNode(type_name=type_name, var_name=var_name, expr=expr_node)
    else:
        var_decl_node_ast = AST.VarDeclNode(type_name=type_name, var_name=var_name)
    
    return var_decl_node_ast


def statement_ast(statement_node: Parser.StatementContext) -> AST.StatementNode:
    if statement_node.if_stat():
        return if_stat_ast(statement_node.if_stat())
    if statement_node.var_decl():
        return var_decl_ast(statement_node.var_decl())
    if statement_node.for_stat():
        return for_stat_ast(statement_node.for_stat())
    if statement_node.while_stat():
        return while_stat_ast(statement_node.while_stat())
    if statement_node.func_call():
        return func_call_ast(statement_node.func_call())
    if statement_node.set_stat():
        return set_stat_ast(statement_node.set_stat())
    return



def if_stat_ast(if_stat_node: Parser.If_statContext) -> AST.IfStatNode:
    expr = expr_ast(if_stat_node.expr())
    block = block_ast(if_stat_node.block())

    if_stat_node_ast = AST.IfStatNode(expr, block)
    return if_stat_node_ast

def for_stat_ast(for_stat_node: Parser.For_statContext) -> AST.ForStatNode:
    counter_var_expr, expr = map(expr_ast, for_stat_node.expr())
    body = block_ast(for_stat_node.block())
    
    return AST.ForStatNode(counter_var_expr, expr, body)

def while_stat_ast(while_stat_node: Parser.While_statContext) -> AST.WhileStatNode:
    condition = expr_ast(while_stat_node.expr())
    block = block_ast(while_stat_node.block())
    return AST.WhileStatNode(condition, block)


def make_func_call_tree(func, args):
    inputs = args[-1].expr()
    if inputs is None: inputs = []
    if type(inputs) is not list: inputs = list(inputs)
    inputs: List[AST.ExprNode] = list(map(expr_ast, inputs))

    if len(args) == 1:
        left_func = func
    else:
        left_func = make_func_call_tree(func, args[0: -1])

    return AST.FuncCallNode(left_func, inputs)

def func_call_ast(func_call_node: Parser.Func_callContext) -> AST.FuncCallNode:
    func_name = class_object_ast(func_call_node.class_object())
    # plus(1)(2)
    args: List[Parser.Func_argsContext] = func_call_node.func_args()
    

    return make_func_call_tree(func_name, args)

def set_stat_ast(set_stat_node: Parser.Set_statContext) -> AST.SetStatNode:
    left, right = map(expr_ast, set_stat_node.expr())
    set_stat_node_ast = AST.SetStatNode(left, right)
    return set_stat_node_ast

# 다항식
def expr_ast(expr_node: Parser.ExprContext) -> AST.ExprNode:
    mult_expr_nodes: List[Parser.MultExprContext] = expr_node.multExpr()
    if type(mult_expr_nodes) != list: mult_expr_nodes = [mult_expr_nodes]
    mult_expr_nodes = list(map(mult_expr_ast, mult_expr_nodes))

    operators: List[str] = []
    children = expr_node.children
    for child in children:
        if type(child) == TerminalNodeImpl:
            operators.append(str(child))
    if len(operators) + 1 != len(mult_expr_nodes):
        raise ValueError("연산자와 대상의 개수가 잘못됨")
    
    expr_node_ast = AST.ExprNode(mult_expr_nodes=mult_expr_nodes, operators=operators)
    return expr_node_ast

# 단항식
def mult_expr_ast(mult_expr_node: Parser.MultExprContext) -> AST.MultExprNode:
    atoms: List[Parser.AtomContext] = mult_expr_node.atom()
    if type(atoms) != list: atoms = list(atoms)
    atoms = list(map(atom_ast, atoms))

    operators: List[str] = []
    children = mult_expr_node.children
    for child in children:
        if type(child) == TerminalNodeImpl:
            operators.append(str(child))
    if len(operators) + 1 != len(atoms):
        raise ValueError("연산자와 대상의 개수가 잘못됨")

    mult_expr_node_ast = AST.MultExprNode(atoms=atoms, operators=operators)
    return mult_expr_node_ast

# 단항식의 원소
def atom_ast(atom_node: Parser.AtomContext) -> AST.AtomNode:
    if atom_node.literal():
        return literal_ast(atom_node.literal())
    if atom_node.expr():
        return expr_ast(atom_node.expr())
    if atom_node.func_call():
        return func_call_ast(atom_node.func_call())
    if atom_node.class_object():
        return class_object_ast(atom_node.class_object())
    if atom_node.condition_value():
        return condition_ast(atom_node.condition_value())
    raise ValueError("Atom Error")
    

def literal_ast(literal_node: Parser.LiteralContext) -> AST.LiteralNode:
    if literal_node.INT():
        return AST.IntLiteralNode(number = int(str(literal_node.INT())))
    if literal_node.STR():
        return AST.StrLiteralNode(string=literal_node.STR())
    return

# A.b.c 꼴
def class_object_ast(class_object_node: Parser.Class_objectContext) -> AST.ClassObjectNode:
    children = class_object_node.children
    if len(children) % 2 == 0: raise ValueError("객체 호출 오류")
    sequence: List[str] = []
    for i in range(0, len(children), 2):
        sequence.append(str(children[i]))
    class_object_node_ast = AST.ClassObjectNode(sequence=sequence)
    return class_object_node_ast

def condition_ast(condition_value_node: Parser.Condition_valueContext) -> AST.ConditionNode:
    condition: Parser.ConditionContext = condition_value_node.condition()
    terms = condition.term()
    if type(terms) is not list: terms = [terms]
    terms = list(map(term_ast, terms))
    return AST.ConditionNode(terms)

def term_ast(term_node : Parser.TermContext) -> AST.TermNode:
    factors = term_node.factor()
    if type(factors) is not list: factors = [factors]
    factors = list(map(factor_ast, factors))
    return AST.TermNode(factors=factors)

def factor_ast(factor_node: Parser.FactorContext) -> AST.FactorNode:
    if factor_node.comparison():
        return AST.FactorNode(comparison=comparison_ast(factor_node.comparison()))
    if factor_node.condition():
        return AST.FactorNode(condition=condition_ast(factor_node.condition()))
    raise ValueError("factor error")

def comparison_ast(comparison_node: Parser.ComparisonContext) -> AST.ComparisonNode:
    left, right = map(expr_ast, comparison_node.expr())
    operator = str(comparison_node.COMPARISON_OPERATOR())
    return AST.ComparisonNode(operator, left, right)
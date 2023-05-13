from parser.ProgramParser import ProgramParser as Parser
from .AST.AST import ASTNode
import semantic_analyizer.AST.ASTNodes as AST
from typing import List
from antlr4.tree.Tree import TerminalNode, TerminalNodeImpl

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
    *input_types, output_type = list(map(lambda x: x.getText(), types))
    func_type_node_ast = AST.FuncTypeNode(input_types=input_types, output_type=output_type)
    #print(input_types, output_type)
    
    # function body
    statements: List[AST.StatementNode] = []
    block_node: Parser.BlockContext = func_decl_node.block()
    
    for statement in block_node.statement():
        statement: Parser.StatementContext
        statements.append(statement_ast(statement))
    
    func_decl_node_ast = AST.FuncDeclNode(func_type=func_type_node_ast, statements=statements)
    return func_decl_node_ast


def var_decl_ast(var_decl_node: Parser.Var_declContext | Parser.Class_var_declContext, class_var = False) -> AST.VarDeclNode:
    if class_var:
        var_decl_node: Parser.Class_var_declContext
    else:
        var_decl_node: Parser.Var_declContext
    
    type_name, var_name, *rest  = list(map(lambda x: x.getText(), var_decl_node.ID()))
    
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
    
    return

def for_stat_ast(for_stat_ast: Parser.For_statContext) -> AST.ForStatNode:
    return

def while_stat_ast(while_stat_ast: Parser.While_statContext) -> AST.WhileStatNode:
    return

def func_call_ast(func_call_ast: Parser.Func_callContext) -> AST.FuncCallNode:
    return

def set_stat_ast(set_stat_ast: Parser.Set_statContext) -> AST.SetStatNode:

    return


def expr_ast(expr_node: Parser.ExprContext) -> AST.ExprNode:
    multExprNodes = expr_node.multExpr()
    if type(multExprNodes) != list: multExprNodes = [multExprNodes]
    operators = expr_node.getTokens()
    print(operators)
    return
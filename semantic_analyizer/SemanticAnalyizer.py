from parser.ProgramParser import ProgramParser as Parser
from .AST.AST import ASTNode
import semantic_analyizer.AST.ASTNodes as AST
from typing import List



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

    if class_decl_node.func_decl():
        for func_decl_node in class_decl_node.func_decl():
            func_decl_node: Parser.Func_declContext
            func_decls.append(func_decl_ast(func_decl_node))
        
    if class_decl_node.class_var_decl():
        for var_decl_node in class_decl_node.class_var_decl():
            var_decl_node: Parser.Var_declContext
            class_var_decls.append(var_decl_ast(var_decl_node=var_decl_node))


    return

def func_decl_ast(first: Parser.Func_declContext) -> AST.FuncDeclNode:
    return

def statement_ast(first: Parser.StatementContext) -> AST.StatementNode:
    return

def var_decl_ast(var_decl_node: Parser.Var_declContext) -> AST.VarDeclNode:
    return



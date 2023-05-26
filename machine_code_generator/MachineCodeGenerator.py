from semantic_analyizer.AST.AST import ASTNode
import semantic_analyizer.AST.ASTNodes as AST
from .MachineCode import MachineCode
from .SymbolTable.SymbolTable import SymbolTable
from typing import List
from .SymbolTable.ObjectSymbol import ObjectSymbol

STATEMENT_CLASSESE = [AST.StatementNode, AST.IfStatNode, AST.ForStatNode, AST.WhileStatNode, AST.SetStatNode, AST.FuncCallNode, AST.VarDeclNode]
DEFAULT_FUNCS = ['return']
symbol_table: SymbolTable

def generate_machine_code(ast: AST.ProgramNode) -> MachineCode:
    global symbol_table
    machine_code = MachineCode()
    symbol_table = SymbolTable()

    class_definitions: List[AST.ClassDeclNode] = []
    func_definitions: List[AST.FuncDeclNode] = []
    statements: List[AST.StatementNode] = []

    for first_node in ast.first_nodes:
        if type(first_node) is AST.ClassDeclNode:
            class_definitions.append(first_node)
        elif type(first_node) is AST.FuncDeclNode:
            func_definitions.append(first_node)
        elif type(first_node) in STATEMENT_CLASSESE:
            statements.append(first_node)
        else:
            raise ValueError(type(first_node))
    
    for class_def in class_definitions:
        symbol_table.add_class(class_def.name)
    for func_def in func_definitions:
        symbol_table.add_func(func_def.name)


    return machine_code

def class_decl(decl: AST.ClassDeclNode, symbol_table: SymbolTable) :
    
    return

# machine_code를 직접 수정
def func_decl(decl: AST.FuncDeclNode, machine_code):
    inputs = zip(decl.args, decl.func_type.input_types)
    symbol_table.decl_func_body(inputs)
    symbol_table.end_decl_func_body()

def generate_statement(statement: AST.StatementNode):
    machine_code = MachineCode()
    d = [(type(statement) is AST.SetStatNode, generate_set_stat), 
         (type(statement) is AST.IfStatNode, generate_if_stat), 
         (type(statement) is AST.ForStatNode, generate_for_stat), 
         (type(statement) is AST.WhileStatNode, genrate_while_stat),
         (type(statement) is AST.FuncCallNode, generate_func_call),
    ]
    error = True
    for x in d: 
        if x[0]: 
            machine_code += x[1](statement)
            error = False
            break
    if error: raise ValueError("Statement Error")
    
    return machine_code

def generate_block(block: AST.BlockNode) -> MachineCode:
    return sum(map(generate_statement, block.statements))

def generate_literal(literal: AST.LiteralNode) -> MachineCode:
    machine_code = MachineCode()
    if type(literal) is AST.IntLiteralNode:
        machine_code.push(literal.number)
    if type(literal) is AST.StrLiteralNode:
        raise ValueError("not implemented")
    return machine_code

def genrate_class_object(class_object: AST.ClassObjectNode) -> MachineCode:
    machine_code = MachineCode()
    parent: ObjectSymbol = symbol_table.get_object(class_object.sequence[0])
    for child in class_object.sequence[1:]:
        if parent.get_var(child):
            parent = parent.get_var(child)
        else:
            raise ValueError("없는 걸 호출했다")
    machine_code.push(parent.get_position())
    return machine_code

def genrate_condition(condition: AST.ConditionNode) -> MachineCode:

    return


def generate_atom(atom: AST.AtomNode) -> MachineCode:
    machine_code = MachineCode()
    d = [(type(atom) in (AST.IntLiteralNode, AST.StrLiteralNode), generate_literal), 
         (type(atom) is AST.ExprNode, generate_expr), 
         (type(atom) is AST.LiteralNode, generate_literal), 
         (type(atom) is AST.ClassObjectNode, genrate_class_object),
         (type(atom) is AST.ConditionNode, genrate_condition),
         (type(atom) is AST.FuncCallNode, generate_func_call),
    ]
    error = True
    for x in d: 
        if x[0]: 
            machine_code += x[1](atom)
            error = False
            break
    if error: raise ValueError("Atom Error")
    
    return machine_code


def generate_mult_expr(mult_expr: AST.MultExprNode) -> MachineCode:
    machine_code = MachineCode()

    first_node_push_code = generate_mult_expr(mult_expr=mult_expr.atoms[0])
    machine_code += first_node_push_code

    for i in range(len(mult_expr.operators)):
        push_code = generate_atom(mult_expr.atoms[i+1])
        machine_code += push_code
        machine_code.do(mult_expr.operators[i])

    return machine_code


def generate_expr(expr: AST.ExprNode) -> MachineCode:
    machine_code = MachineCode()

    first_node_push_code = generate_mult_expr(mult_expr=expr.mult_expr_nodes[0])
    machine_code += first_node_push_code

    for i in range(len(expr.operators)):
        push_code = generate_mult_expr(expr.mult_expr_nodes[i+1])
        machine_code += push_code
        machine_code.do(expr.operators[i])

    return machine_code


def generate_func_call(func_call: AST.FuncCallNode):
    machine_code = MachineCode()
    name = func_call.func_name
    for func_input in func_call.inputs:
        machine_code += generate_expr(func_input) # 스택에 추가하는 명령
    
    if name in DEFAULT_FUNCS:
        # 분기
        if name == "return":
            pass
        else:
            machine_code.do(name)
    else:
        machine_code += symbol_table.func_use(name) # func_use 함수는 스택에서 입력값을 제거해야 함
        return machine_code


def generate_set_stat(set_stat: AST.SetStatNode) -> MachineCode:
    machine_code = MachineCode()
    machine_code.do(symbol_table.get_object(set_stat.left).get_position())
    machine_code += generate_expr(set_stat.right)
    machine_code.do('=')
    return machine_code


def generate_if_stat(if_stat: AST.IfStatNode) -> MachineCode:
    machine_code = MachineCode()
    machine_code += generate_expr(symbol_table.get_object(if_stat.expr))
    machine_code.if_(generate_block(if_stat.block))
    return
def generate_for_stat(for_stat: AST.ForStatNode) -> MachineCode:
    
    return
def genrate_while_stat(while_stat: AST.WhileStatNode) -> MachineCode:
    return
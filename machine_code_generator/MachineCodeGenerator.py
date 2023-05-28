from semantic_analyizer.AST.AST import ASTNode
import semantic_analyizer.AST.ASTNodes as AST
from .MachineCode import *
from .SymbolTable.SymbolTable import SymbolTable
from .SymbolTable.FuncSymbol import FuncSymbol
from .SymbolTable.ObjectSymbol import ObjectSymbol
from .SymbolTable.ClassSymbol import ClassSymbol
from typing import List

STATEMENT_CLASSESE = [AST.StatementNode, AST.IfStatNode, AST.ForStatNode, AST.WhileStatNode, AST.SetStatNode, AST.FuncCallNode, AST.VarDeclNode]
DEFAULT_FUNCS = {'return': go_back(), 'print': print_()}
MACHINECODE_FUNC_FOR_STR = {'<' : less(), '>': greater(), '<=': less_or_equal(), '>=': greater_or_equal(), '==': equal()}
MACHINECODE_FUNC_FOR_OPERATORS = {'+': plus(), '-': minus(), '*': multiply(), '/': divide()}

symbol_table: SymbolTable

def generate_machine_code(ast: AST.ProgramNode) -> MachineCode:
    global symbol_table
    machine_code = MachineCode()
    symbol_table = SymbolTable()

    machine_code.append(go(value(-1)))

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
        symbol_table.add_class(class_def.name, ClassSymbol())
    for func_def in func_definitions:
        symbol_table.add_func(func_def.name, FuncSymbol(func_def.name, func_def.func_type))


    for func_def in func_definitions:
        machine_code += func_decl(func_def, machine_code.lines.__len__())
    machine_code.lines[0] = go(value(len(machine_code.lines)))
    for statement in statements:
        machine_code += generate_statement(statement)

    machine_code.check_points()

    return machine_code

def class_decl(decl: AST.ClassDeclNode, symbol_table: SymbolTable) :
    
    return

def func_decl(decl: AST.FuncDeclNode, line: int):
    machine_code = MachineCode()

    inputs = zip(decl.args, decl.func_type.input_types)
    symbol_table.decl_func_body(symbol_table.functions[decl.name], inputs)

    block = generate_block(decl.block)
    machine_code += block

    symbol_table.end_decl_func_body()
    symbol_table.functions[decl.name].index = line
    symbol_table.functions[decl.name].memory_size = len(decl.args)
    

    return machine_code

def generate_statement(statement: AST.StatementNode):
    machine_code = MachineCode()
    d = [(type(statement) is AST.SetStatNode, generate_set_stat), 
         (type(statement) is AST.IfStatNode, generate_if_stat), 
         (type(statement) is AST.ForStatNode, generate_for_stat), 
         (type(statement) is AST.WhileStatNode, genrate_while_stat),
         (type(statement) is AST.FuncCallNode, generate_func_call),
         (type(statement) is AST.VarDeclNode, generate_var_decl),
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
    a = MachineCode()
    for code in map(generate_statement, block.statements):
        a += code
    return a

def generate_literal(literal: AST.LiteralNode) -> MachineCode:
    machine_code = MachineCode()
    if type(literal) is AST.IntLiteralNode:
        machine_code.append(put(value(literal.number)))
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
    machine_code.append(put(parent.get_position()))
    return machine_code

def genrate_condition(condition: AST.ConditionNode) -> MachineCode:
    machine_code = MachineCode()
    terms: AST.TermNode = condition.terms
    for term in terms:
        factors: AST.FactorNode = term.factors
        for factor in factors:
            if factor.condition is None and factor.comparison is not None:
                # comparison
                comparison = factor.comparison
                left_expr = generate_expr(comparison.left_expr)
                right_expr = generate_expr(comparison.right_expr)
                operater = MACHINECODE_FUNC_FOR_STR[comparison.operator]

                machine_code += left_expr
                machine_code += right_expr

                machine_code.append(do(operater))
            
            elif factor.condition is not None and factor.comparison is None:
                # condidion
                return genrate_condition(factor.condition)
            
            else:
                raise ValueError("Both are")
        
        for i in range(len(factors) - 1):
            machine_code.append(do(and_()))
    
    for i in range(len(terms) - 1):
        machine_code.append(do(or_()))
    
    return machine_code


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

    first_node_push_code = generate_atom(mult_expr.atoms[0])
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
        machine_code.append(do(MACHINECODE_FUNC_FOR_OPERATORS[expr.operators[i]]))

    return machine_code


def generate_func_call(func_call: AST.FuncCallNode):
    machine_code = MachineCode()

    names = func_call.func_name.sequence
    for func_input in func_call.inputs:
        machine_code += generate_expr(func_input) # 스택에 추가하는 명령
    
    if len(names) == 1 and names[0] in DEFAULT_FUNCS:
        if names[0] == "return":
            machine_code.append(go_back())
            pass
        else:
            machine_code.append(do(DEFAULT_FUNCS[names[0]]))
    elif len(names) == 1:
        func = symbol_table.functions[names[0]]
        machine_code.append([MachineCode.POINT, func])
    else:
        parent: ObjectSymbol = symbol_table.get_object(names.sequence[0])
        for child in names[1:-1]:
            if parent.get_var(child):
                parent = parent.get_var(child)
            else:
                raise ValueError("없는 걸 호출했다")

        func:FuncSymbol = parent.get_class().get_func(names.sequence[-1])
        machine_code.add_point(func)

    return machine_code


def generate_set_stat(set_stat: AST.SetStatNode) -> MachineCode:
    machine_code = MachineCode()
    machine_code.do(symbol_table.get_object(set_stat.left).get_position())
    machine_code += generate_expr(set_stat.right)
    machine_code.do('=')
    return machine_code


def generate_if_stat(if_stat: AST.IfStatNode) -> MachineCode:
    machine_code = MachineCode()
    condition = generate_expr(if_stat.expr)
    block = generate_block(if_stat.block)

    machine_code += condition
    block_length = len(block.lines)
    machine_code.append(else_skip(value(block_length)))

    machine_code += block

    return machine_code

def generate_for_stat(for_stat: AST.ForStatNode) -> MachineCode:
    
    return
def genrate_while_stat(while_stat: AST.WhileStatNode) -> MachineCode:
    return



def generate_var_decl(var_decl: AST.VarDeclNode) -> MachineCode:
    machine_code = MachineCode()
    var = ObjectSymbol(var_decl.var_name, var_decl.type_name) 
    symbol_table.add_var(var_decl.var_name, var)

    if var_decl.expr is not None:
        machine_code += generate_expr(var_decl.expr)
    

    return machine_code
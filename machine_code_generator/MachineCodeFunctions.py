from .MachineCode import MachineCode
from typing import List

def put(value: List[int]) -> List[int]:
    return [MachineCode.PUT] + value
def pop() -> List[int]:
    return [MachineCode.POP]

def index(index: int) -> List[int]:
    return [MachineCode.INDEX, index]

def value(value: int) -> List[int]:
    return [MachineCode.VALUE, value]

def do(func: List[int]) -> List[int]:
    return [MachineCode.DO] + func

def equal():
    return [MachineCode.EQUAL]
def less():
    return [MachineCode.LESS]
def greater():
    return [MachineCode.GREATER]
def less_or_equal():
    return [MachineCode.LESSOREQUAL]
def greater_or_equal():
    return [MachineCode.GREATEROREQUAL]


def else_skip(num: List[int]) -> List[int]:
    return [MachineCode.ELSESKIP] + num

def go_back() -> List[int]:
    return [MachineCode.GOBACK]

def func_call(index: List[int], args: List[int]) -> List[int]:
    return [MachineCode.FUNCCALL] + index + args

def go(index: List[int]) -> List[int]:
    return [MachineCode.GO] + index

def plus():
    return [MachineCode.PLUS]
def minus():
    return [MachineCode.MINUS]
def multiply():
    return [MachineCode.MULTIPLY]
def divide():
    return [MachineCode.DIVIDE]
def print_():
    return [MachineCode.PRINT]
from typing import List
from machine_code_generator.SymbolTable.FuncSymbol import FuncSymbol
dictionary = [
    'DO',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',

    'PUT',
    'POP',
    'ELSESKIP',
    'GOBACK',
    'FUNCCALL',
    'GO',

    'INDEX',
    'VALUE',

    'EQUAL',
    'LESS',
    'GREATER',
    'LESSOREQUAL',
    'GREATEROREQUAL',

    'PRINT',
    'OR',
    'AND',
    'NOT',

    'POINT'
]

class MachineCode:
    def __init__(self, *lines: List[List[int]]) -> None:
        self.lines:List[List[int]] = []
        if lines is not None and lines.__len__() > 0:
            self.lines = lines[0]
        
        self.points = []
        pass
    
    # 미래에 넣을 거
    def add_point(self, item):
        self.points.append((self.lines.__len__(), item))

    def check_points(self):
        i = 0
        for line in self.lines:
            if line[0] == MachineCode.POINT:
                func = line[1]
                self.lines[i] = func_call(value(func.index_line()), value(func.get_memory_size()))
            i += 1
        """
        for point in self.points:
            index, func = point
            func: FuncSymbol
            line = func_call(value(func.index_line()), value(func.get_memory_size()))
            self.lines.insert(index, line)"""

    def append(self, line: List[int]):
        self.lines.append(line)
    

    def __add__(self, other):
        machine_code =MachineCode()
        machine_code.lines = self.lines
        machine_code.lines += other.lines
        for point in self.points:
            machine_code.points.append(point)
        for point in other.points:
            machine_code.points.append((point[0] + self.lines.__len__(), point[1]))
        return machine_code

    def __str__(self) -> str:
        string = ""
        for line in self.lines:
            words = []
            is_value = False
            is_index = False
            for word in line:
                if word == MachineCode.VALUE:
                    is_value = True
                elif word == MachineCode.INDEX:
                    is_index = True
                elif is_value:
                    is_value = False
                    words.append(str(word))
                elif is_index:
                    is_index = False
                    words.append('&' + str(word))
                else:
                    words.append(dictionary[word])
            string += " ".join(words) + "\n"
                
        return string
    
    
    DO = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4

    PUT = 5
    POP = 6
    ELSESKIP = 7
    GOBACK = 8
    FUNCCALL = 9
    GO = 10

    INDEX = 11
    VALUE = 12

    EQUAL = 13
    LESS = 14
    GREATER = 15
    LESSOREQUAL = 16
    GREATEROREQUAL = 17

    PRINT = 18

    OR = 19
    AND = 20
    NOT = 21

    POINT = 22 # 컴파일러 전용



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

def or_():
    return [MachineCode.OR]
def and_():
    return [MachineCode.AND]
def not_():
    return [MachineCode.NOT]
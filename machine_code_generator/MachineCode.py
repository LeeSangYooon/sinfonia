from typing import List
class MachineCode:
    def __init__(self, *lines: List[List[int]]) -> None:
        self.lines = lines[0]
        pass
    def do(self) -> None:
        return
    def push(self) -> None:
        return
    def __str__(self) -> str:
        return "not yet"
    
    
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


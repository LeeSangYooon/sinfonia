from .ObjectSymbol import ObjectSymbol
from typing import List, Tuple
class SymbolTable:
    def __init__(self) -> None:
        self.classes = []
        self.functions = []
        pass

    def add_class(self, name: str):
        self.classes.append(name)

    def add_func(self, name: str):
        self.functions.append(name)
    
    def get_object(self, name:str) -> ObjectSymbol:
        return
    
    def decl_func_body(inputs: List[Tuple[str, str]]):
        return

    def end_decl_func_body():
        return
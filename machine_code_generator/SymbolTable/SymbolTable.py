from .ObjectSymbol import ObjectSymbol
from .FuncSymbol import FuncSymbol
from .ClassSymbol import ClassSymbol
from typing import List, Tuple, TypedDict
from machine_code_generator.MachineCode import index

class SymbolTable:
    def __init__(self) -> None:
        self.classes = dict()
        self.functions = dict()
        self.objects: List[TypedDict[str, ObjectSymbol]] = [dict()]
        self.open_func = []
        pass

    def add_class(self, name: str, class_symbol: ClassSymbol):
        self.classes[name] = class_symbol

    def add_func(self, name: str, func_symbol: FuncSymbol):
        self.functions[name] = func_symbol
    
    def add_var(self, name:str, object_symbol: ObjectSymbol):
        self.objects[-1][name] = object_symbol
        object_symbol.machine_code_index = index(self.objects[-1].__len__() - 1)
        
        if len(self.open_func) > 0: # else: first level
            self.open_func[-1].memory_size += 1

    def get_object(self, name:str) -> ObjectSymbol:
        return self.objects[-1][name]
    
    def decl_func_body(self, func:FuncSymbol, inputs: List[Tuple[str, str]]):
        self.objects.append(dict())
        i = 0
        for ipt in inputs:
            var_name, var_type = ipt
            obj = ObjectSymbol(var_name, var_type)
            if var_name in self.objects[-1]:
                raise ValueError("")
            self.objects[-1][var_name] = obj
            obj.machine_code_index = index(i)
            i += 1
        self.open_func.append(func)
        return

    def end_decl_func_body(self):
        self.objects.pop()
        self.open_func.pop()
        return
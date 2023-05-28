from .ClassSymbol import ClassSymbol
from .Type import Type
class ObjectSymbol:
    def __init__(self, name:str, obj_type: Type) -> None:
        self.class_symbol: ClassSymbol
        self.machine_code_index:str = None
        self.obj_type = obj_type
        self.name = name
    def get_var(self, name:str):
        return
    def get_func(self, name:str):
        return
    def get_class(self):
        return
    def get_position(self) :
        if self.machine_code_index is None: raise ValueError()
        return self.machine_code_index
from .Type import Type

class FuncSymbol:
    def __init__(self, name:str, obj_type:Type) -> None:

        self.index = None
        self.memory_size = None
        pass

    def index_line(self) -> int:
        return self.index
    
    def get_memory_size(self) -> int:
        return self.memory_size
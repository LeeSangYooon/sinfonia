
class ClassSymbol:
    def __init__(self) -> None:
        self.functions = dict()
        pass

    def get_func(self, name:str):
        return self.functions[name]

    
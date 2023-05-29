from machine_code_generator.MachineCode import MachineCode

# Virtual Machine
class VirtualMachine:
    def __init__(self) -> None:
        self.line = None
        self.pointer = None
        self.code = None
        self.length = None

        self.stack = None
        self.memory_pivot = None
        pass
    
    def consume(self, num:int = 1) -> None:
        self.pointer += num
        if self.pointer < len(self.code):
            self.line = self.code[self.pointer]
        else:
            pass
            #print("done")
    
    def done(self) -> None:
        return self.pointer >= self.length
    
    def get_value(self, index: int):
        if self.line[index] == MachineCode.VALUE:
            return self.line[index + 1]
        return self.stack[self.line[index + 1] + self.memory_pivot[-1]]
    
    def is_true(self, value):
        return value == 1
    
    def do(self, operation):
        if operation == MachineCode.PLUS:
            self.stack.append(self.stack.pop() + self.stack.pop())
        elif operation == MachineCode.MINUS:
            self.stack.append(-self.stack.pop() + self.stack.pop())
        elif operation == MachineCode.MULTIPLY:
            self.stack.append(self.stack.pop() * self.stack.pop())
        elif operation == MachineCode.DIVIDE:
            self.stack.append(1 / self.stack.pop() * self.stack.pop())
        elif operation == MachineCode.PRINT:
            print(self.stack.pop())
        elif operation == MachineCode.EQUAL:
            self.stack.append(self.stack.pop() == self.stack.pop())
        elif operation == MachineCode.LESS:
            self.stack.append(self.stack.pop() > self.stack.pop())
        elif operation == MachineCode.GREATER:
            self.stack.append(self.stack.pop() < self.stack.pop())
        elif operation == MachineCode.LESSOREQUAL:
            self.stack.append(self.stack.pop() >= self.stack.pop())
        elif operation == MachineCode.GREATEROREQUAL:
            self.stack.append(self.stack.pop() <= self.stack.pop())
        else:
            raise ValueError("not implemented")



    def run(self, virtual_machine_code: MachineCode) -> None:
        self.code = virtual_machine_code.lines
        self.length = len(self.code)
        self.stack =[]
        self.call_stack = []
        self.args_stack = []
        self.func_memory = []
        self.func_return_existence = []
        self.memory_pivot = [0]
        self.pointer = 0
        self.line = self.code[0]

        while not self.done():
            self.line = self.code[self.pointer]
            #print(self.pointer, self.line, self.stack)
            if self.line[0] == MachineCode.PUT:
                self.stack.append(self.get_value(1))
            elif self.line[0] == MachineCode.POP:
                self.stack.pop()

            elif self.line[0] == MachineCode.SET:
                self.stack[self.line[2] + self.memory_pivot[-1]] = self.stack.pop()

            
            elif self.line[0] == MachineCode.ELSESKIP:
                if not self.is_true(self.stack.pop()):
                    self.consume(self.get_value(1))

            elif self.line[0] == MachineCode.GOBACK:
                # 함수 입력값 제거
                if self.func_return_existence[-1]:
                    top = self.stack.pop() # 함수 리턴값
                    for i in range(self.func_memory.pop()):
                        self.stack.pop()
                    self.stack.append(top)
                else:
                    for i in range(self.func_memory.pop()):
                        self.stack.pop()


                self.pointer = self.call_stack.pop()
                self.memory_pivot.pop()
                self.func_return_existence.pop()
                self.args_stack.pop()
                continue

            elif self.line[0] == MachineCode.FUNCCALL:
                self.call_stack.append(self.pointer + 1)
                self.pointer = self.line[1]
                self.memory_pivot.append(len(self.stack) - self.line[2])
                self.args_stack.append(self.line[2])
                self.func_memory.append(self.line[3])
                self.func_return_existence.append(self.line[4])
                continue

            elif self.line[0] == MachineCode.GO:
                self.pointer = self.get_value(1)
                continue
            
            elif self.line[0] == MachineCode.DO:
                self.do(self.line[1])
            else:
                raise ValueError("not implemented")
            self.consume()

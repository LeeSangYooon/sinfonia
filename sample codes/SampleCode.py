from machine_code_generator.MachineCode import *

multiply_machine_code = MachineCode([
    go(value(15)),

    put(index(1)),
    put(value(0)),
    do(equal()),

    else_skip(value(2)),
    put(value(0)),
    go_back(),

    put(index(0)),

    put(index(0)),

    put(index(1)),
    put(value(1)),
    do(minus()),

    func_call(value(1), value(2)),

    do(plus()),

    go_back(),

    put(value(4)),
    put(value(0)),
    func_call(value(1), value(2)),
    do(print_()),
])
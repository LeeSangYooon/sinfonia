from time import time
from sys import stdout
def timer(name:str, func):
    stdout.write(name+'......')
    t = time()
    ret = func()
    stdout.write(f' done in {time() - t} seconds\n')
    return ret

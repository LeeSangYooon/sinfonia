from antlr4 import *
from parser.ProgramLexer import ProgramLexer
from parser.ProgramParser import ProgramParser
from typing import *

def parse(code: str) -> tuple[ProgramParser.ProgContext, Parser]:
    lexer = ProgramLexer(InputStream(code))
    parser = ProgramParser(CommonTokenStream(lexer))
    parse_tree = parser.prog()
    #first : ProgramParser.FirstContext = parse_tree.first()[0]
    #classdecl: ProgramParser.Class_declContext = first.class_decl()
    #print(classdecl.func_decl())
    return parse_tree, parser
    # print(parse_tree.toStringTree(recog=parser))


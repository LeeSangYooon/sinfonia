# Generated from Program.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,2,1,
        2,5,2,56,8,2,10,2,12,2,59,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,5,4,71,8,4,10,4,12,4,74,9,4,1,4,1,4,1,4,1,5,1,5,5,5,81,8,5,
        10,5,12,5,84,9,5,1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,107,8,8,1,9,1,9,
        1,9,1,9,3,9,113,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,5,14,138,8,14,10,14,12,14,141,9,14,1,15,1,15,1,15,5,15,146,8,
        15,10,15,12,15,149,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        3,16,159,8,16,1,17,1,17,5,17,163,8,17,10,17,12,17,166,9,17,1,18,
        1,18,1,18,4,18,171,8,18,11,18,12,18,172,1,19,1,19,1,19,0,0,20,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,1,1,0,12,
        13,178,0,41,1,0,0,0,2,48,1,0,0,0,4,50,1,0,0,0,6,62,1,0,0,0,8,66,
        1,0,0,0,10,78,1,0,0,0,12,85,1,0,0,0,14,94,1,0,0,0,16,106,1,0,0,0,
        18,108,1,0,0,0,20,116,1,0,0,0,22,120,1,0,0,0,24,125,1,0,0,0,26,129,
        1,0,0,0,28,134,1,0,0,0,30,142,1,0,0,0,32,158,1,0,0,0,34,160,1,0,
        0,0,36,167,1,0,0,0,38,174,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,
        43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,1,1,0,0,0,45,49,3,4,2,
        0,46,49,3,6,3,0,47,49,3,16,8,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,
        1,0,0,0,49,3,1,0,0,0,50,51,5,1,0,0,51,52,5,18,0,0,52,57,5,2,0,0,
        53,56,3,6,3,0,54,56,3,14,7,0,55,53,1,0,0,0,55,54,1,0,0,0,56,59,1,
        0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,
        61,5,3,0,0,61,5,1,0,0,0,62,63,3,8,4,0,63,64,3,10,5,0,64,65,3,12,
        6,0,65,7,1,0,0,0,66,67,5,4,0,0,67,72,5,18,0,0,68,69,5,5,0,0,69,71,
        5,18,0,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,6,0,0,76,77,5,18,0,0,77,9,1,
        0,0,0,78,82,5,18,0,0,79,81,5,18,0,0,80,79,1,0,0,0,81,84,1,0,0,0,
        82,80,1,0,0,0,82,83,1,0,0,0,83,11,1,0,0,0,84,82,1,0,0,0,85,89,5,
        2,0,0,86,88,3,16,8,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,
        90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,3,0,0,93,13,1,0,0,
        0,94,95,5,18,0,0,95,96,5,18,0,0,96,97,5,7,0,0,97,15,1,0,0,0,98,107,
        3,18,9,0,99,107,3,20,10,0,100,107,3,22,11,0,101,107,3,24,12,0,102,
        103,3,34,17,0,103,104,5,7,0,0,104,107,1,0,0,0,105,107,3,26,13,0,
        106,98,1,0,0,0,106,99,1,0,0,0,106,100,1,0,0,0,106,101,1,0,0,0,106,
        102,1,0,0,0,106,105,1,0,0,0,107,17,1,0,0,0,108,109,5,18,0,0,109,
        112,5,18,0,0,110,111,5,8,0,0,111,113,3,28,14,0,112,110,1,0,0,0,112,
        113,1,0,0,0,113,114,1,0,0,0,114,115,5,7,0,0,115,19,1,0,0,0,116,117,
        5,9,0,0,117,118,3,28,14,0,118,119,3,12,6,0,119,21,1,0,0,0,120,121,
        5,10,0,0,121,122,5,18,0,0,122,123,3,28,14,0,123,124,3,12,6,0,124,
        23,1,0,0,0,125,126,5,11,0,0,126,127,3,28,14,0,127,128,3,12,6,0,128,
        25,1,0,0,0,129,130,3,28,14,0,130,131,5,8,0,0,131,132,3,28,14,0,132,
        133,5,7,0,0,133,27,1,0,0,0,134,139,3,30,15,0,135,136,7,0,0,0,136,
        138,3,30,15,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,
        140,1,0,0,0,140,29,1,0,0,0,141,139,1,0,0,0,142,147,3,32,16,0,143,
        144,5,14,0,0,144,146,3,32,16,0,145,143,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,31,1,0,0,0,149,147,1,0,0,0,150,159,
        3,38,19,0,151,159,5,18,0,0,152,153,5,15,0,0,153,154,3,28,14,0,154,
        155,5,16,0,0,155,159,1,0,0,0,156,159,3,34,17,0,157,159,3,36,18,0,
        158,150,1,0,0,0,158,151,1,0,0,0,158,152,1,0,0,0,158,156,1,0,0,0,
        158,157,1,0,0,0,159,33,1,0,0,0,160,164,5,18,0,0,161,163,3,28,14,
        0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,
        0,165,35,1,0,0,0,166,164,1,0,0,0,167,170,5,18,0,0,168,169,5,17,0,
        0,169,171,5,18,0,0,170,168,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,
        0,172,173,1,0,0,0,173,37,1,0,0,0,174,175,5,19,0,0,175,39,1,0,0,0,
        14,43,48,55,57,72,82,89,106,112,139,147,158,164,172
    ]

class ProgramParser ( Parser ):

    grammarFileName = "Program.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class '", "'{'", "'}'", "'#'", "','", 
                     "'->'", "';'", "'='", "'if'", "'for'", "'while'", "'+'", 
                     "'-'", "'*'", "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_first = 1
    RULE_class_decl = 2
    RULE_func_decl = 3
    RULE_func_type = 4
    RULE_func_head = 5
    RULE_block = 6
    RULE_class_var_decl = 7
    RULE_statement = 8
    RULE_var_decl = 9
    RULE_if_stat = 10
    RULE_for_stat = 11
    RULE_while_stat = 12
    RULE_set_stat = 13
    RULE_expr = 14
    RULE_multExpr = 15
    RULE_atom = 16
    RULE_func_call = 17
    RULE_class_object = 18
    RULE_literal = 19

    ruleNames =  [ "prog", "first", "class_decl", "func_decl", "func_type", 
                   "func_head", "block", "class_var_decl", "statement", 
                   "var_decl", "if_stat", "for_stat", "while_stat", "set_stat", 
                   "expr", "multExpr", "atom", "func_call", "class_object", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ID=18
    INT=19
    NEWLINE=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def first(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.FirstContext)
            else:
                return self.getTypedRuleContext(ProgramParser.FirstContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ProgramParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.first()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 822802) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FirstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(ProgramParser.Class_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ProgramParser.Func_declContext,0)


        def statement(self):
            return self.getTypedRuleContext(ProgramParser.StatementContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_first

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirst" ):
                listener.enterFirst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirst" ):
                listener.exitFirst(self)




    def first(self):

        localctx = ProgramParser.FirstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_first)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.class_decl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.func_decl()
                pass
            elif token in [9, 10, 11, 15, 18, 19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ProgramParser.ID, 0)

        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.Func_declContext)
            else:
                return self.getTypedRuleContext(ProgramParser.Func_declContext,i)


        def class_var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.Class_var_declContext)
            else:
                return self.getTypedRuleContext(ProgramParser.Class_var_declContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_class_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_decl" ):
                listener.enterClass_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_decl" ):
                listener.exitClass_decl(self)




    def class_decl(self):

        localctx = ProgramParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ProgramParser.T__0)
            self.state = 51
            self.match(ProgramParser.ID)
            self.state = 52
            self.match(ProgramParser.T__1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==18:
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 53
                    self.func_decl()
                    pass
                elif token in [18]:
                    self.state = 54
                    self.class_var_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(ProgramParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_type(self):
            return self.getTypedRuleContext(ProgramParser.Func_typeContext,0)


        def func_head(self):
            return self.getTypedRuleContext(ProgramParser.Func_headContext,0)


        def block(self):
            return self.getTypedRuleContext(ProgramParser.BlockContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)




    def func_decl(self):

        localctx = ProgramParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.func_type()
            self.state = 63
            self.func_head()
            self.state = 64
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.ID)
            else:
                return self.getToken(ProgramParser.ID, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_func_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_type" ):
                listener.enterFunc_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_type" ):
                listener.exitFunc_type(self)




    def func_type(self):

        localctx = ProgramParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ProgramParser.T__3)
            self.state = 67
            self.match(ProgramParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 68
                self.match(ProgramParser.T__4)
                self.state = 69
                self.match(ProgramParser.ID)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(ProgramParser.T__5)
            self.state = 76
            self.match(ProgramParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_headContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.ID)
            else:
                return self.getToken(ProgramParser.ID, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_func_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_head" ):
                listener.enterFunc_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_head" ):
                listener.exitFunc_head(self)




    def func_head(self):

        localctx = ProgramParser.Func_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ProgramParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 79
                self.match(ProgramParser.ID)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProgramParser.StatementContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ProgramParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ProgramParser.T__1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 822784) != 0):
                self.state = 86
                self.statement()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(ProgramParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.ID)
            else:
                return self.getToken(ProgramParser.ID, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_class_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_var_decl" ):
                listener.enterClass_var_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_var_decl" ):
                listener.exitClass_var_decl(self)




    def class_var_decl(self):

        localctx = ProgramParser.Class_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_class_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ProgramParser.ID)
            self.state = 95
            self.match(ProgramParser.ID)
            self.state = 96
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ProgramParser.Var_declContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(ProgramParser.If_statContext,0)


        def for_stat(self):
            return self.getTypedRuleContext(ProgramParser.For_statContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(ProgramParser.While_statContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ProgramParser.Func_callContext,0)


        def set_stat(self):
            return self.getTypedRuleContext(ProgramParser.Set_statContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ProgramParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.if_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.for_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.while_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.func_call()
                self.state = 103
                self.match(ProgramParser.T__6)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.set_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.ID)
            else:
                return self.getToken(ProgramParser.ID, i)

        def expr(self):
            return self.getTypedRuleContext(ProgramParser.ExprContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = ProgramParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ProgramParser.ID)
            self.state = 109
            self.match(ProgramParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 110
                self.match(ProgramParser.T__7)
                self.state = 111
                self.expr()


            self.state = 114
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProgramParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(ProgramParser.BlockContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)




    def if_stat(self):

        localctx = ProgramParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ProgramParser.T__8)
            self.state = 117
            self.expr()
            self.state = 118
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ProgramParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ProgramParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(ProgramParser.BlockContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_for_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stat" ):
                listener.enterFor_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stat" ):
                listener.exitFor_stat(self)




    def for_stat(self):

        localctx = ProgramParser.For_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ProgramParser.T__9)
            self.state = 121
            self.match(ProgramParser.ID)
            self.state = 122
            self.expr()
            self.state = 123
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ProgramParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(ProgramParser.BlockContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)




    def while_stat(self):

        localctx = ProgramParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ProgramParser.T__10)
            self.state = 126
            self.expr()
            self.state = 127
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProgramParser.ExprContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_set_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_stat" ):
                listener.enterSet_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_stat" ):
                listener.exitSet_stat(self)




    def set_stat(self):

        localctx = ProgramParser.Set_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_set_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.expr()
            self.state = 130
            self.match(ProgramParser.T__7)
            self.state = 131
            self.expr()
            self.state = 132
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.MultExprContext)
            else:
                return self.getTypedRuleContext(ProgramParser.MultExprContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ProgramParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.multExpr()
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 135
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 136
                    self.multExpr() 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.AtomContext)
            else:
                return self.getTypedRuleContext(ProgramParser.AtomContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_multExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpr" ):
                listener.enterMultExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpr" ):
                listener.exitMultExpr(self)




    def multExpr(self):

        localctx = ProgramParser.MultExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.atom()
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.match(ProgramParser.T__13)
                    self.state = 144
                    self.atom() 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ProgramParser.LiteralContext,0)


        def ID(self):
            return self.getToken(ProgramParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ProgramParser.ExprContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ProgramParser.Func_callContext,0)


        def class_object(self):
            return self.getTypedRuleContext(ProgramParser.Class_objectContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = ProgramParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(ProgramParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.match(ProgramParser.T__14)
                self.state = 153
                self.expr()
                self.state = 154
                self.match(ProgramParser.T__15)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 157
                self.class_object()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ProgramParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProgramParser.ExprContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = ProgramParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ProgramParser.ID)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.expr() 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.ID)
            else:
                return self.getToken(ProgramParser.ID, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_class_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_object" ):
                listener.enterClass_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_object" ):
                listener.exitClass_object(self)




    def class_object(self):

        localctx = ProgramParser.Class_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_class_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ProgramParser.ID)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.match(ProgramParser.T__16)
                self.state = 169
                self.match(ProgramParser.ID)
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==17):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ProgramParser.INT, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ProgramParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ProgramParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






# Generated from Program.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ProgramParser import ProgramParser
else:
    from ProgramParser import ProgramParser

# This class defines a complete listener for a parse tree produced by ProgramParser.
class ProgramListener(ParseTreeListener):

    # Enter a parse tree produced by ProgramParser#prog.
    def enterProg(self, ctx:ProgramParser.ProgContext):
        pass

    # Exit a parse tree produced by ProgramParser#prog.
    def exitProg(self, ctx:ProgramParser.ProgContext):
        pass


    # Enter a parse tree produced by ProgramParser#first.
    def enterFirst(self, ctx:ProgramParser.FirstContext):
        pass

    # Exit a parse tree produced by ProgramParser#first.
    def exitFirst(self, ctx:ProgramParser.FirstContext):
        pass


    # Enter a parse tree produced by ProgramParser#class_decl.
    def enterClass_decl(self, ctx:ProgramParser.Class_declContext):
        pass

    # Exit a parse tree produced by ProgramParser#class_decl.
    def exitClass_decl(self, ctx:ProgramParser.Class_declContext):
        pass


    # Enter a parse tree produced by ProgramParser#func_decl.
    def enterFunc_decl(self, ctx:ProgramParser.Func_declContext):
        pass

    # Exit a parse tree produced by ProgramParser#func_decl.
    def exitFunc_decl(self, ctx:ProgramParser.Func_declContext):
        pass


    # Enter a parse tree produced by ProgramParser#func_type.
    def enterFunc_type(self, ctx:ProgramParser.Func_typeContext):
        pass

    # Exit a parse tree produced by ProgramParser#func_type.
    def exitFunc_type(self, ctx:ProgramParser.Func_typeContext):
        pass


    # Enter a parse tree produced by ProgramParser#func_head.
    def enterFunc_head(self, ctx:ProgramParser.Func_headContext):
        pass

    # Exit a parse tree produced by ProgramParser#func_head.
    def exitFunc_head(self, ctx:ProgramParser.Func_headContext):
        pass


    # Enter a parse tree produced by ProgramParser#block.
    def enterBlock(self, ctx:ProgramParser.BlockContext):
        pass

    # Exit a parse tree produced by ProgramParser#block.
    def exitBlock(self, ctx:ProgramParser.BlockContext):
        pass


    # Enter a parse tree produced by ProgramParser#class_var_decl.
    def enterClass_var_decl(self, ctx:ProgramParser.Class_var_declContext):
        pass

    # Exit a parse tree produced by ProgramParser#class_var_decl.
    def exitClass_var_decl(self, ctx:ProgramParser.Class_var_declContext):
        pass


    # Enter a parse tree produced by ProgramParser#statement.
    def enterStatement(self, ctx:ProgramParser.StatementContext):
        pass

    # Exit a parse tree produced by ProgramParser#statement.
    def exitStatement(self, ctx:ProgramParser.StatementContext):
        pass


    # Enter a parse tree produced by ProgramParser#var_decl.
    def enterVar_decl(self, ctx:ProgramParser.Var_declContext):
        pass

    # Exit a parse tree produced by ProgramParser#var_decl.
    def exitVar_decl(self, ctx:ProgramParser.Var_declContext):
        pass


    # Enter a parse tree produced by ProgramParser#if_stat.
    def enterIf_stat(self, ctx:ProgramParser.If_statContext):
        pass

    # Exit a parse tree produced by ProgramParser#if_stat.
    def exitIf_stat(self, ctx:ProgramParser.If_statContext):
        pass


    # Enter a parse tree produced by ProgramParser#for_stat.
    def enterFor_stat(self, ctx:ProgramParser.For_statContext):
        pass

    # Exit a parse tree produced by ProgramParser#for_stat.
    def exitFor_stat(self, ctx:ProgramParser.For_statContext):
        pass


    # Enter a parse tree produced by ProgramParser#while_stat.
    def enterWhile_stat(self, ctx:ProgramParser.While_statContext):
        pass

    # Exit a parse tree produced by ProgramParser#while_stat.
    def exitWhile_stat(self, ctx:ProgramParser.While_statContext):
        pass


    # Enter a parse tree produced by ProgramParser#set_stat.
    def enterSet_stat(self, ctx:ProgramParser.Set_statContext):
        pass

    # Exit a parse tree produced by ProgramParser#set_stat.
    def exitSet_stat(self, ctx:ProgramParser.Set_statContext):
        pass


    # Enter a parse tree produced by ProgramParser#condition.
    def enterCondition(self, ctx:ProgramParser.ConditionContext):
        pass

    # Exit a parse tree produced by ProgramParser#condition.
    def exitCondition(self, ctx:ProgramParser.ConditionContext):
        pass


    # Enter a parse tree produced by ProgramParser#term.
    def enterTerm(self, ctx:ProgramParser.TermContext):
        pass

    # Exit a parse tree produced by ProgramParser#term.
    def exitTerm(self, ctx:ProgramParser.TermContext):
        pass


    # Enter a parse tree produced by ProgramParser#factor.
    def enterFactor(self, ctx:ProgramParser.FactorContext):
        pass

    # Exit a parse tree produced by ProgramParser#factor.
    def exitFactor(self, ctx:ProgramParser.FactorContext):
        pass


    # Enter a parse tree produced by ProgramParser#comparison.
    def enterComparison(self, ctx:ProgramParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ProgramParser#comparison.
    def exitComparison(self, ctx:ProgramParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ProgramParser#condition_value.
    def enterCondition_value(self, ctx:ProgramParser.Condition_valueContext):
        pass

    # Exit a parse tree produced by ProgramParser#condition_value.
    def exitCondition_value(self, ctx:ProgramParser.Condition_valueContext):
        pass


    # Enter a parse tree produced by ProgramParser#expr.
    def enterExpr(self, ctx:ProgramParser.ExprContext):
        pass

    # Exit a parse tree produced by ProgramParser#expr.
    def exitExpr(self, ctx:ProgramParser.ExprContext):
        pass


    # Enter a parse tree produced by ProgramParser#multExpr.
    def enterMultExpr(self, ctx:ProgramParser.MultExprContext):
        pass

    # Exit a parse tree produced by ProgramParser#multExpr.
    def exitMultExpr(self, ctx:ProgramParser.MultExprContext):
        pass


    # Enter a parse tree produced by ProgramParser#atom.
    def enterAtom(self, ctx:ProgramParser.AtomContext):
        pass

    # Exit a parse tree produced by ProgramParser#atom.
    def exitAtom(self, ctx:ProgramParser.AtomContext):
        pass


    # Enter a parse tree produced by ProgramParser#func_args.
    def enterFunc_args(self, ctx:ProgramParser.Func_argsContext):
        pass

    # Exit a parse tree produced by ProgramParser#func_args.
    def exitFunc_args(self, ctx:ProgramParser.Func_argsContext):
        pass


    # Enter a parse tree produced by ProgramParser#func_call.
    def enterFunc_call(self, ctx:ProgramParser.Func_callContext):
        pass

    # Exit a parse tree produced by ProgramParser#func_call.
    def exitFunc_call(self, ctx:ProgramParser.Func_callContext):
        pass


    # Enter a parse tree produced by ProgramParser#class_object.
    def enterClass_object(self, ctx:ProgramParser.Class_objectContext):
        pass

    # Exit a parse tree produced by ProgramParser#class_object.
    def exitClass_object(self, ctx:ProgramParser.Class_objectContext):
        pass


    # Enter a parse tree produced by ProgramParser#literal.
    def enterLiteral(self, ctx:ProgramParser.LiteralContext):
        pass

    # Exit a parse tree produced by ProgramParser#literal.
    def exitLiteral(self, ctx:ProgramParser.LiteralContext):
        pass



del ProgramParser
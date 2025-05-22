# Generated from src/Arithmetic.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#prog.
    def enterProg(self, ctx:ArithmeticParser.ProgContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#prog.
    def exitProg(self, ctx:ArithmeticParser.ProgContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#ExprStmt.
    def enterExprStmt(self, ctx:ArithmeticParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#ExprStmt.
    def exitExprStmt(self, ctx:ArithmeticParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#AssignStmt.
    def enterAssignStmt(self, ctx:ArithmeticParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#AssignStmt.
    def exitAssignStmt(self, ctx:ArithmeticParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Variable.
    def enterVariable(self, ctx:ArithmeticParser.VariableContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Variable.
    def exitVariable(self, ctx:ArithmeticParser.VariableContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Number.
    def enterNumber(self, ctx:ArithmeticParser.NumberContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Number.
    def exitNumber(self, ctx:ArithmeticParser.NumberContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#MulDiv.
    def enterMulDiv(self, ctx:ArithmeticParser.MulDivContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#MulDiv.
    def exitMulDiv(self, ctx:ArithmeticParser.MulDivContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#AddSub.
    def enterAddSub(self, ctx:ArithmeticParser.AddSubContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#AddSub.
    def exitAddSub(self, ctx:ArithmeticParser.AddSubContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Parens.
    def enterParens(self, ctx:ArithmeticParser.ParensContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Parens.
    def exitParens(self, ctx:ArithmeticParser.ParensContext):
        pass



del ArithmeticParser
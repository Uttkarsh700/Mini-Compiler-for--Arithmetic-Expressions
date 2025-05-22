from antlr4 import *
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generated.ArithmeticLexer import ArithmeticLexer
from generated.ArithmeticParser import ArithmeticParser
from generated.ArithmeticListener import ArithmeticListener

class PostfixListener(ArithmeticListener):
    def __init__(self):
        self.postfix_stack = []
        self.temp_counter = 0
        self.three_address_code = []
        self.is_assignment = False
        self.assignment_var = None
        self.last_temp = None

    def get_temp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        self.last_temp = temp
        return temp

    def exitAssignStmt(self, ctx):
        # Get the variable name
        self.assignment_var = ctx.ID().getText()
        self.is_assignment = True

    def exitMulDiv(self, ctx):
        right = self.postfix_stack.pop()
        left = self.postfix_stack.pop()
        op = ctx.getChild(1).getText()
        
        # For postfix notation
        self.postfix_stack.append(f"{left} {right} {op}")
        
        # For three-address code
        temp = self.get_temp()
        self.three_address_code.append(f"{temp} = {left} {op} {right}")
        ctx.temp = temp

    def exitAddSub(self, ctx):
        right = self.postfix_stack.pop()
        left = self.postfix_stack.pop()
        op = ctx.getChild(1).getText()
        
        # For postfix notation
        self.postfix_stack.append(f"{left} {right} {op}")
        
        # For three-address code
        temp = self.get_temp()
        self.three_address_code.append(f"{temp} = {left} {op} {right}")
        ctx.temp = temp

    def exitVariable(self, ctx):
        self.postfix_stack.append(ctx.getText())
        ctx.temp = ctx.getText()

    def exitNumber(self, ctx):
        self.postfix_stack.append(ctx.getText())
        ctx.temp = ctx.getText()

    def exitProg(self, ctx):
        if self.is_assignment:
            # Get the value from the stack
            value = self.postfix_stack[-1]
            # Add the assignment to three-address code using the last temporary variable
            if self.last_temp:
                self.three_address_code.append(f"{self.assignment_var} = {self.last_temp}")
            else:
                self.three_address_code.append(f"{self.assignment_var} = {value}")
            # Update postfix to show correct order: value var =
            self.postfix_stack[-1] = f"{value} {self.assignment_var} ="

class Compiler:
    def __init__(self):
        self.lexer = None
        self.parser = None
        self.tree = None
        self.walker = None
        self.listener = None

    def compile(self, input_text):
        # Create lexer and parser
        input_stream = InputStream(input_text)
        self.lexer = ArithmeticLexer(input_stream)
        token_stream = CommonTokenStream(self.lexer)
        self.parser = ArithmeticParser(token_stream)
        
        # Parse the input
        self.tree = self.parser.prog()
        
        # Create and use the listener
        self.listener = PostfixListener()
        self.walker = ParseTreeWalker()
        self.walker.walk(self.listener, self.tree)
        
        return {
            'postfix': self.listener.postfix_stack[-1] if self.listener.postfix_stack else '',
            'three_address_code': self.listener.three_address_code
        }

def main():
    compiler = Compiler()
    while True:
        try:
            text = input('Enter expression (or "quit" to exit): ')
            if text.lower() == 'quit':
                break
                
            result = compiler.compile(text)
            print("\nPostfix notation:")
            print(result['postfix'])
            print("\nThree-address code:")
            for code in result['three_address_code']:
                print(code)
            print()
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    main() 
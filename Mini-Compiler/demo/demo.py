import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.compiler import Compiler

def print_header():
    print("=" * 50)
    print("Mini Compiler Demo - Arithmetic Expressions")
    print("=" * 50)
    print("\nThis demo allows you to enter arithmetic expressions")
    print("and see their postfix notation and three-address code.")
    print("\nExample expressions:")
    print("  a + b * c")
    print("  (a + b) * c")
    print("  a * b + c * d")
    print("\nType 'quit' to exit")
    print("=" * 50)

def main():
    print_header()
    compiler = Compiler()
    
    while True:
        try:
            print("\nEnter an expression:")
            text = input("> ").strip()
            
            if text.lower() == 'quit':
                print("\nGoodbye!")
                break
                
            if not text:
                continue
                
            result = compiler.compile(text)
            
            print("\nResults:")
            print("-" * 20)
            print("Postfix notation:")
            print(result['postfix'])
            print("\nThree-address code:")
            for code in result['three_address_code']:
                print(code)
            print("-" * 20)
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again with a valid expression.")

if __name__ == '__main__':
    main() 
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.compiler import Compiler

def run_test(expression, expected_postfix, expected_code):
    compiler = Compiler()
    result = compiler.compile(expression)
    
    postfix_match = result['postfix'] == expected_postfix
    code_match = result['three_address_code'] == expected_code
    
    print(f"\nTest: {expression}")
    print(f"Expected postfix: {expected_postfix}")
    print(f"Got postfix: {result['postfix']}")
    print(f"Expected code: {expected_code}")
    print(f"Got code: {result['three_address_code']}")
    print(f"Test {'PASSED' if postfix_match and code_match else 'FAILED'}")
    
    return postfix_match and code_match

def main():
    tests = [
        {
            'expression': 'a + b * c',
            'expected_postfix': 'a b c * +',
            'expected_code': ['t0 = b * c', 't1 = a + t0']
        },
        {
            'expression': '(a + b) * c',
            'expected_postfix': 'a b + c *',
            'expected_code': ['t0 = a + b', 't1 = t0 * c']
        },
        {
            'expression': 'a * b + c * d',
            'expected_postfix': 'a b * c d * +',
            'expected_code': ['t0 = a * b', 't1 = c * d', 't2 = t0 + t1']
        }
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if run_test(test['expression'], test['expected_postfix'], test['expected_code']):
            passed += 1
    
    print(f"\nTest Summary: {passed}/{total} tests passed")

if __name__ == '__main__':
    main() 
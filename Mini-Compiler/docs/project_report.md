# Mini Compiler Project Report

## Overview

This project implements a mini compiler for arithmetic expressions that converts infix notation to postfix notation and generates three-address code. The implementation uses ANTLR4 for parsing and Python for the compiler logic.

## Architecture

### Components

1. **Grammar Definition** (`Arithmetic.g4`)
   - Defines the syntax for arithmetic expressions
   - Supports basic operations: +, -, *, /
   - Handles variables and numbers
   - Includes parentheses for grouping

2. **Compiler Implementation** (`compiler.py`)
   - `PostfixListener`: ANTLR listener that generates postfix notation
   - `Compiler`: Main class that orchestrates the compilation process
   - Handles error cases and provides meaningful error messages

3. **Testing** (`test_script.py`)
   - Automated test suite
   - Tests various expression types
   - Verifies postfix notation and three-address code generation

4. **Demo Application** (`demo.py`)
   - Interactive command-line interface
   - Real-time expression evaluation
   - User-friendly output formatting

## Implementation Details

### Grammar Rules

The grammar is defined in ANTLR4 format with the following rules:
- `prog`: Entry point for the grammar
- `expr`: Expression rules with operator precedence
- `ID`: Variable names (alphanumeric)
- `NUMBER`: Integer and floating-point numbers
- `WS`: Whitespace handling

### Compilation Process

1. **Lexical Analysis**
   - Input text is tokenized using ANTLR4 lexer
   - Tokens are identified (operators, variables, numbers)

2. **Parsing**
   - ANTLR4 parser creates a parse tree
   - Operator precedence is handled automatically

3. **Postfix Generation**
   - `PostfixListener` traverses the parse tree
   - Builds postfix notation using a stack-like approach

4. **Three-Address Code Generation**
   - Temporary variables are created for intermediate results
   - Code is generated in a linear sequence

## Usage Examples

### Basic Expression
Input: `a + b * c`
Postfix: `a b c * +`
Three-address code:
```
t0 = b * c
t1 = a + t0
```

### Expression with Parentheses
Input: `(a + b) * c`
Postfix: `a b + c *`
Three-address code:
```
t0 = a + b
t1 = t0 * c
```

## Testing

The test suite includes:
- Basic arithmetic operations
- Operator precedence
- Parentheses handling
- Multiple operations
- Error cases

## Future Improvements

1. **Error Handling**
   - More detailed error messages
   - Recovery from syntax errors

2. **Optimization**
   - Constant folding
   - Common subexpression elimination

3. **Features**
   - Support for more operators
   - Variable assignment
   - Function calls

4. **User Interface**
   - Graphical interface
   - Syntax highlighting
   - Real-time compilation

## Conclusion

The mini compiler successfully implements the core functionality of converting arithmetic expressions to postfix notation and generating three-address code. The modular design allows for easy extension and maintenance. 
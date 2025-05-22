# Mini Compiler for Arithmetic Expressions

A professional-grade compiler that processes arithmetic expressions, converts them to postfix notation, and generates three-address code. This project demonstrates fundamental compiler concepts including lexical analysis, parsing, and code generation.

## Features

- **Lexical Analysis**: Tokenizes input expressions using ANTLR4
- **Syntax Analysis**: Parses expressions with proper operator precedence
- **Code Generation**: 
  - Converts infix expressions to postfix notation
  - Generates three-address code
- **Error Handling**: Graceful error reporting for invalid expressions
- **Testing**: Comprehensive test suite
- **Interactive Demo**: User-friendly command-line interface

## Prerequisites

- Python 3.x
- Java Runtime Environment (JRE)
- ANTLR 4.9.2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mini-compiler.git
cd mini-compiler
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Download ANTLR 4.9.2:
```bash
# Windows
curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar

# Linux/Mac
wget https://www.antlr.org/download/antlr-4.9.2-complete.jar
```

4. Generate the ANTLR parser:
```bash
java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 -o src/generated src/Arithmetic.g4
```

## Usage

### Running the Demo

```bash
python demo/demo.py
```

Example session:
```
==================================================
Mini Compiler Demo - Arithmetic Expressions
==================================================

Enter an expression:
> a + b * c

Results:
--------------------
Postfix notation:
a b c * +

Three-address code:
t0 = b * c
t1 = a + t0
--------------------
```

### Running Tests

```bash
python tests/test_script.py
```

## Project Structure

```
mini-compiler/
├── src/                    # Source code
│   ├── Arithmetic.g4       # ANTLR grammar definition
│   ├── compiler.py         # Main compiler implementation
│   └── generated/          # Generated ANTLR files
├── tests/                  # Test files
│   ├── test_script.py     # Test suite
│   └── test_cases.txt     # Test cases
├── docs/                   # Documentation
│   └── project_report.md  # Detailed project documentation
├── demo/                   # Demo application
│   ├── demo.py           # Interactive demo
│   └── demo_output.txt   # Sample outputs
├── antlr-4.9.2-complete.jar
├── README.md
├── requirements.txt
└── .gitignore
```

## Examples

### Basic Arithmetic

Input: `a + b * c`
```
Postfix: a b c * +
Three-address code:
t0 = b * c
t1 = a + t0
```

### Parentheses

Input: `(a + b) * c`
```
Postfix: a b + c *
Three-address code:
t0 = a + b
t1 = t0 * c
```

### Multiple Operations

Input: `a * b + c * d`
```
Postfix: a b * c d * +
Three-address code:
t0 = a * b
t1 = c * d
t2 = t0 + t1
```

## Implementation Details

### Grammar Rules

The compiler uses ANTLR4 grammar with the following rules:
- `prog`: Entry point for the grammar
- `expr`: Expression rules with operator precedence
- `ID`: Variable names (alphanumeric)
- `NUMBER`: Integer and floating-point numbers
- `WS`: Whitespace handling

### Compilation Process

1. **Lexical Analysis**: Input is tokenized into operators, variables, and numbers
2. **Parsing**: ANTLR4 creates a parse tree respecting operator precedence
3. **Postfix Generation**: Tree is traversed to generate postfix notation
4. **Code Generation**: Three-address code is generated using temporary variables

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ANTLR4 for the parser generator
- Python community for excellent tools and libraries 
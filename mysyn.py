import mylex
import ply.yacc as yacc
from mylex import tokens

def p_create_table(p):
    '''create_table : CREATE TABLE ID LPAREN column_definitions RPAREN SEMICOLON'''
    # Process the CREATE TABLE command
    print("CREATE TABLE command parsed successfully")


def p_column_definitions(p):
    '''column_definitions : column_definition
                          | column_definition COMMA column_definitions'''


def p_column_definition(p):
    '''column_definition : ID TYPE
                         | ID TYPE NULL
                         | ID TYPE PRIMARY KEY
                         | ID TYPE DEFAULT expression
                         | ID TYPE REFERENCES ID
                         | FOREIGN KEY LPAREN ID RPAREN REFERENCES ID LPAREN ID RPAREN'''


def p_expression_id(t):
    'expression : ID'
    t[0] = t[1]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

# Error rule for syntax errors
def p_error(p):
    # if p is None:
    #     pass
    print(f"Syntax error at {p.value} and {p.lineno}")


# Build the parser
parser = yacc.yacc(debug=True)

# Test the parser

data = ""
while True:
    x = input()
    if x.__contains__(';'):
        data+=x
        break
    else:
        data += x

result = parser.parse(data)
print(result)

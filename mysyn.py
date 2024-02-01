import mylex
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from mylex import tokens

def p_create_table(p):
    """create_table : CREATE TABLE ID LPAREN column_definitions RPAREN SEMICOLON"""
    # Process the CREATE TABLE command
    print("CREATE TABLE command parsed successfully")


def p_column_definitions(p):
    """column_definitions : column_definition
                          | column_definition COMMA column_definitions"""


def p_column_definition(p):
    """column_definition : ID TYPE
                         | ID TYPE LPAREN NUMBER RPAREN
                         | ID TYPE NULL
                         | ID TYPE PRIMARY KEY
                         | ID TYPE DEFAULT expression
                         | ID TYPE REFERENCES ID"""


def p_expression(p):
    """expression : NUMBER
                  | STRING"""


# Error rule for syntax errors
def p_error(p):
    print("Syntax error")


# Build the parser
parser = yacc.yacc()

# Test the parser

result = parser.parse("CREATE TABLE TableName (ID INT, Name VARCHAR(255), Age INT);")
print(result)

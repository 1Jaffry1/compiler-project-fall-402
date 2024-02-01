from ply import lex

# List of token names
tokens = (
    'CREATE',
    'TABLE',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'ID',
    'TYPE',
    'NUMBER',
    'SEMICOLON',
    'PRIMARY',
    'FOREIGN',
    'KEY',
    'NULL',
    'DATE',
    'CHECK',
    'GREATER',
    'EQUAL',
    'DEFAULT',
    'REFERENCES',
    'ON',
    'DELETE',
    'SET',
    'CASCADE',
    'UNIQUE',
    'IN',
    'UPDATE',
    'TIME'
)

# Regular expression rules for simple tokens
# t_CREATE = r'CREATE'
# t_TABLE = r'TABLE'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ignore = ' \t\n'
t_SEMICOLON = r';'
# t_KEY = r'KEY'
# t_NULL = r'NULL'
# t_DATE = r'DATE'
# t_CHECK = r'CHECK'
# t_GREATER = r'>'
# t_EQUAL = r'='
# t_DEFAULT = r'DEFAULT'
# t_REFERENCES = r'REFERENCES'
# t_ON = r'ON'
# t_DELETE = r'DELETE'
# t_SET = r'SET'
# t_CASCADE = r'CASCADE'
# t_UNIQUE = r'UNIQUE'
# t_IN = r'IN'
# t_UPDATE = r'UPDATE'
# t_TIME = r'TIME'

# State variable to track whether type has been assigned
type_assigned = False


# Define a rule for data types (for simplicity, just identifying them as TYPE tokens)
def t_TYPE(t):
    r'INT|VARCHAR|TEXT|FLOAT|DATE|TIME|BOOLEAN|NUMBER|BIT|SMALLINT|INT|BIGINT|REAL|FLOAT|DECIMAL|CHAR|NCHAR|NVARCHAR|TEXT|BINARY'
    # Set the state variable to True when a type is assigned
    global type_assigned
    type_assigned = True
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Regular expression rule for ID
def t_ID(t):
    r'[a-z|A-Z|0-9|_][a-z|A-Z|0-9|_]*'
    # Check if type has not been assigned
    if not type_assigned:
        return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
data = ""
while True:
    x = input()
    if x.__contains__(";"):
        data += x
        break
    data += x

# Reset the type_assigned variable before processing input
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

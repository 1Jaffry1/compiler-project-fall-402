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
    'keytype',
    'KEY'
)

# Regular expression rules for simple tokens
t_CREATE = r'CREATE'
t_TABLE = r'TABLE'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ignore = ' \t\n'
t_SEMICOLON = r';'
t_keytype = r'FOREIGN+PRIMARY'
t_KEY = r'KEY'


# Define a rule for data types (for simplicity, just identifying them as TYPE tokens)
def t_TYPE(t):
    r'INT|VARCHAR|TEXT|FLOAT|DATE|TIME|BOOLEAN|NUMBER'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in tokens:
        t.type = t.value.upper()  # Convert reserved words to uppercase
    return t

# Build the lexer
lexer = lex.lex()
# Test the lexer


data = ""
while True:
    x = input()
    if x.__contains__(";"):
        data += x
        break
    data += x
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

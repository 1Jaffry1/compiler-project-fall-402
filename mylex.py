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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ignore = ' \t\n'
t_SEMICOLON = r';'




def t_TYPE(t):
    r"""INT|VARCHAR|TEXT|FLOAT|DATE|TIME|BOOLEAN|NUMBER|BIT|SMALLINT|INT|BIGINT|REAL|FLOAT|DECIMAL|CHAR|NCHAR|NVARCHAR
    |TEXT|BINARY"""
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
        t.type = t.value.upper()
    return t

lexer = lex.lex()
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
import ply.yacc as yacc
import mylex
import tkinter as tk
from tkinter import messagebox
from mylex import tokens

msg = ""
err_cnt=0
erline = -1
erchar = -1


def p_create_tables(p):
    '''create_tables : create_table
                     | create_tables create_table'''


def p_create_table(p):
    '''create_table : CREATE TABLE ID REF LPAREN column_definitions RPAREN SEMICOLON'''

def p_REF(p):
    '''REF : REFERENCES ID
            | empty'''
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


def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global msg, err_cnt
    msg += f"\nSyntax error at token \"{p.value}\": line {mylex.line_number}, pos {p.lexpos - mylex.index}" + '\n'
    err_cnt+=1



parser = yacc.yacc(debug=True)


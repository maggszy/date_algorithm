from helpy import *
import operator
import string
import time
from typing import Any, List, Optional, Tuple, Union

operators = ['+', '-', '*', '/', '^']
functions = ['sin(', 'cos(', 'ln(', 'exp(', 'sqrt(']   # takes one argument
brackets = ["(", ")"]

letters = set(string.ascii_lowercase).union(set(string.ascii_uppercase)).union({"pi"})


def parsing(expression):
    expr_list = list(expression)
    elems = []
    funcs = set(operators + functions + brackets)
    for chars in sorted(funcs.union(letters), key=len, reverse=True):
        find = True
        chars_len = len(chars)
        while find:
            try:
                occur_ind = "".join(expr_list).index(chars)
                expr_list[occur_ind: occur_ind + chars_len] = [" "] * chars_len
                elems.append([occur_ind, chars])
            except ValueError:
                find = False

    nums = "".join(expr_list).split()

    for num in nums:
        occur_ind = "".join(expr_list).index(num)
        expr_list[occur_ind: occur_ind + chars_len] = [" "] * chars_len
        elems.append([occur_ind, num])

    result = []
    elems_dict = dict(elems)
    for ind in sorted(elems_dict):
        result.append(elems_dict[ind])

    return result


def expression_tree(formula):
    """ Function to represent list of characters as a tree.
        Represents brackets, functions, operators and numerical values."""
    
    stack = Stack()
    b_tree = BinaryTree('')
    stack.push(b_tree)
    tmp_tree = b_tree

    for i in formula:
        if i == '(':
            tmp_tree.insert_left('')
            stack.push(tmp_tree)
            tmp_tree = tmp_tree.get_left_child()
            # print(i,'--->')#,b_tree)
        elif i == ')': 
            tmp_tree = stack.pop()  
            # print(i,'--->')#,b_tree)
        elif i in operators or i in functions:
            tmp_tree.set_root_val(i)
            tmp_tree.insert_right('')
            stack.push(tmp_tree)
            tmp_tree = tmp_tree.get_right_child()
            # parent = stack.pop()
            # tmp_tree = parent
            # print(i,'--->')#,b_tree)
        elif i not in operators and i not in functions and i not in brackets:
            tmp_tree.set_root_val(i)
            parent = stack.pop()
            tmp_tree = parent
            # print(i,'--->')#,b_tree)

    return b_tree

def derivation(tree):

    dtree = BinaryTree('')

    if tree.get_root_val() == '+':
        derivation(tree.get_left_child())
        derivation(tree.get_right_child())

    elif tree.get_root_val() == '-':
        derivation(tree.get_left_child())
        derivation(tree.get_right_child())

    elif tree.get_root_val() == '*':
        dtree.set_root_val('+')
        dtree.insert_left('*')
        dtree.insert_right('*')
        derivation(tree.get_right_child())
        derivation(tree.get_left_child())

    elif tree.get_root_val() == '/':
        dtree.set_root_val('/')
        dtree.insert_left('-')
        dtree.insert_right('^')
        dtree = dtree.get_left_child()
        dtree.insert_left('*')
        dtree.insert_right('*')

def expr_tree(formula):
    pass

def printexp(tree):
    string_val = ""
    if tree:
        string_val = '(' + printexp(tree.get_left_child())
        string_val = string_val + str(tree.get_root_val())
        string_val = string_val + printexp(tree.get_right_child())+')'
    return string_val

# formula2 = parsing('(((-1)*2*(5+x))/sin(x))')
formula = parsing('((2*(5+x))/sin(x))')
# fomula = '(2*(sin(x)))/(5+x))'
print(formula)
pt = expression_tree(formula)
#print(derivation(pt))
print(printexp(pt))
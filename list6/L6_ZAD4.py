from helpy import *
import operator
import string
import time
from typing import Any, List, Optional, Tuple, Union

operators = ['+', '-', '*', '/', '^']
functions = ['sin', 'cos', 'ln', 'exp', 'sqrt']   # takes one argument
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
    tmp_tree = BinaryTree('')
    stack.push(tmp_tree)

    for i in formula:
        if i == '(':
            tmp_tree.insert_left('')
            stack.push(tmp_tree)
            tmp_tree = tmp_tree.get_left_child()
        elif i == ')':
            tmp_tree = stack.pop()
        elif i in operators or i in functions:
            tmp_tree.set_root_val(i)
            tmp_tree.insert_right('')
            stack.push(tmp_tree)
            tmp_tree = tmp_tree.get_right_child()
        elif i not in operators and i not in functions and i not in brackets:
            tmp_tree.set_root_val(i)
            parent = stack.pop()
            tmp_tree = parent

    return tmp_tree


def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def printexp(tree):
    string_val = ""
    if tree:
        string_val = '(' + printexp(tree.get_left_child())
        string_val = string_val + str(tree.get_root_val())
        string_val = string_val + printexp(tree.get_right_child())+')'
    return string_val


formula = parsing('(2*x)/(5+x)')
print(formula)
pt = expression_tree(formula)
print(inorder(pt))
# print(printexp(pt))
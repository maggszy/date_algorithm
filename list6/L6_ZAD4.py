from helpy import *
import string

operators = ['+', '-', '*', '/', '^']
functions = ['sin', 'cos', 'ln', 'exp']   # takes one argument
brackets = ["(", ")"]
letters = set(string.ascii_lowercase).union({"pi"})


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

    return b_tree


def derivation(tree, var):

    dtree = BinaryTree('')
    pstack = Stack()
    pstack.push(dtree)

    if tree.get_root_val() in ['+', '-']:
        dtree.left_child = derivation(tree.get_left_child(), var)
        dtree.right_child = derivation(tree.get_right_child(), var)
        if tree.get_root_val() == '+':
            dtree.set_root_val('+')
        else:
            dtree.set_root_val('-')

    elif tree.get_root_val() == '*':
        dtree.set_root_val('+')
        dtree.insert_left('*')
        pstack.push(dtree)
        dtree = dtree.get_left_child()
        dtree.insert_left(derivation(tree.get_left_child(), var))
        dtree.insert_right(tree.get_right_child())
        dtree = pstack.pop()

        dtree.insert_right('*')
        pstack.push(dtree)
        dtree = dtree.get_right_child()
        dtree.insert_left(tree.get_left_child())
        dtree.insert_right(derivation(tree.get_right_child(), var))
        dtree = pstack.pop()

    elif tree.get_root_val() == '/':
        dtree.set_root_val('/')
        dtree.insert_left('-')
        pstack.push()
        dtree = dtree.get_left_child()

        dtree.insert_left('*')
        pstack.push()
        dtree = dtree.get_left_child()

        dtree.insert_left(derivation(tree.get_left_child(), var))
        dtree.insert_right(tree.get_right_child())
        dtree = pstack.pop()

        dtree.insert_right('*')
        pstack.push(dtree)
        dtree = dtree.get_right_child()

        dtree.insert_left(tree.get_left_child())
        dtree.insert_right(derivation(tree.get_right_child(), var))
        pstack.pop()
        dtree = pstack.pop()

        #jeste??my znowu w '/', dodajemy prawe poddrzewo
        dtree.insert_right('^')
        pstack.push(dtree)
        dtree = dtree.get_right_child()

        dtree.insert_left(tree.get_right_child())
        dtree.insert_right('2')
        dtree = pstack.pop()

    elif tree.get_root_val() == "^":
        dtree.set_root_val("*")
        dtree.insert_left('*')
        dtree.insert_right(derivation(tree.get_left_child()))

        pstack.push(dtree)
        dtree = dtree.get_left_child()
        dtree.insert_left(tree.get_right_child())
        dtree.insert_right("^")

        pstack.push(dtree)
        dtree = dtree.get_right_child()

        dtree.insert_left(tree.get_left_child())
        dtree.insert_right(tree.get_right_child() - 1)
        pstack.pop()
        dtree = pstack.pop()

        pstack.push(dtree)
        dtree = dtree.get_left_child()

    elif tree.get_root_val() == 'sin':
        dtree.set_root_val("*")

        dtree.insert_right('cos')
        dtree.insert_left(derivation(tree.get_right_child(), var))
        pstack.push(dtree)
        dtree = dtree.get_right_child()

        dtree.insert_right(tree.get_right_child())
        dtree = pstack.pop()

    elif tree.get_root_val() == 'cos':
        dtree.set_root_val("*")

        dtree.insert_right('*')
        dtree.insert_left(derivation(tree.get_right_child(), var))
        pstack.push(dtree)
        dtree = dtree.get_right_child()

        dtree.insert_left(-1)
        dtree.insert_right("sin")
        pstack.push(dtree)
        dtree = dtree.get_right_child()

        dtree.insert_right(tree.get_right_child())
        pstack.pop()
        dtree = pstack.pop()

    elif tree.get_root_val() == 'ln':
        dtree.set_root_val("/")
        dtree.insert_left(derivation(tree.get_right_child(), var))
        dtree.insert_right(tree.get_right_child())

    elif tree.get_root_val() == 'exp':
        dtree.set_root_val("*")
        dtree.insert_left(derivation(tree.get_right_child(), var))
        dtree.insert_right('exp')

        pstack.push(dtree)
        dtree = dtree.get_right_child()
        dtree.insert_right(tree.get_right_child())
        dtree = pstack.pop()

    else:
        if tree.get_root_val() == var:
            dtree.set_root_val(1)
        else:
            dtree.set_root_val(0)

    return dtree


def printexp(tree):
    string_val = ""
    if tree:
        string_val = '(' + printexp(tree.get_left_child())
        string_val = string_val + str(tree.get_root_val())
        string_val = string_val + printexp(tree.get_right_child())+')'
    return string_val





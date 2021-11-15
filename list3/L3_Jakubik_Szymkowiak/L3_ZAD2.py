import time

def ordinary_polynomial_value_calc(coeff, arg):
    """
    Calculate value of polynomial in a standart way
    :param coeff: a list with coefficients of polynomial positioned from free term to the term of the highest degree
    :param arg: the value of variable x in polynomial W(x)
    :return: tuple with the value of polynomial and amout of executed multiplication and addition
    """
    if not isinstance(coeff,list):
        raise TypeError("Variable 'coeff' should be a list")
        
    if type(arg) not in {int,float}:
        raise TypeError("Variable 'arg' should be an int or float")
    
    if coeff==[]:
        raise ValueError("Lack of coefficients, fill list with numvers!")
    
    n=len(coeff)
    count_add=0
    count_mult=0
    value=coeff[0]
    for dg in range(1,n):
        value=coeff[dg]*(arg**dg) + value
        count_mult+=dg
        count_add+=1
    return value, count_mult, count_add
  
def smart_polynomial_value_calc(coeff, arg):
    """
    Calculate value of polynomial using the Horner's algorithm
    :param coeff: a list with coefficients of polynomial positioned from free term to the term of the highest degree
    :param arg: the value of variable x in polynomial W(x)
    :return: tuple with the value of polynomial and amout of executed multiplication and addition
    """
    if not isinstance(coeff,list):
        raise TypeError("Variable 'coeff' should be a list")
        
    if type(arg) not in {int,float}:
        raise TypeError("Variable 'arg' should be an int or float")
    
    if coeff==[]:
        raise ValueError("Lack of coefficients, fill list with numvers!")
        
    n=len(coeff)
    coeff.reverse() 
    value=coeff[0]
    count_mult=0
    for dg in range(1,n): #dg=degree
        value = value*arg + coeff[dg]
        count_mult+=1
    count_add=count_mult
    return value, count_mult, count_add

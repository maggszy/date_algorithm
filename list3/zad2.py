def ordinary_polynomial_value_calc(coeff, arg):
    n=len(coeff)
    count_add=0
    count_mult=0
    value=coeff[0]
    for dg in range(1,n):
        value=coeff[dg]*arg**dg + value
        count_mult+=dg
        count_add+=1
    return value, count_mult, count_add
  
def smart_polynomial_value_calc(coeff, arg):
    n=len(coeff)
    coeff.reverse() 
    value=coeff[0]
    count_mult=0
    for dg in range(1,n): #dg=degree
        value = value*arg + coeff[dg]
        count_mult+=1
    count_add=count_mult
    return value, count_mult, count_add


print(smart_polynomial_value_calc([1,2,3,4], 2))
print(ordinary_polynomial_value_calc([1,2,3,4], 2))
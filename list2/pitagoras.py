import math
import time

def pytha_triplet(nums_sum):  #n^3
    operation_count=0
    for a in range(1,nums_sum):
        for b in range(1,nums_sum):
            for c in range(1,nums_sum):
                operation_count+=9
                if a**2 + b**2 == c**2 and a+b+c==nums_sum:
                    return(True,a,b,c,operation_count)
    return (False,-1,-1,-1,operation_count)


def pytha_triplet2(nums_sum):  #n^2
    operation_count=0
    for a in range(1,nums_sum//3):
        for b in range(a+1,nums_sum//2):
            c=nums_sum-a-b
            operation_count+=14
            if a**2 + b**2 == c**2 and a+b+c==nums_sum:
               return(True,a,b,c,operation_count)

    return (False,-1,-1,-1,operation_count) 

def pytha_triplet3(nums_sum): #n
    operation_count=0
    for c in range(1,nums_sum):
        a_b_sqr= c**2 - nums_sum**2 + 2*nums_sum*c
        a_b= math.floor(math.sqrt(abs(a_b_sqr)))
        operation_count+=7

        if a_b**2 == a_b_sqr:
            b=(nums_sum - c + a_b)//2
            a= nums_sum - b - c
            operation_count+=8
            return(True,a,b,c,operation_count)
        else:
            operation_count+=3


    return (False,-1,-1,-1,operation_count) 




print(pytha_triplet2(200))
print(pytha_triplet2(20))
print(pytha_triplet3(200))
#print(pytha_triplet(200))
#print(pytha_triplet(1000))
print(pytha_triplet(12))
from utily import gcd

#not sure about zad7

class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den

        #common = gcd(self.num, self.den)
        #self.num=self.num/common  #do rozkminienia
        #self.den==self.den/common

        if type(self.num) != int:
            raise TypeError('Numerator must be integers') #not sure if they're atributs

        if type(self.den) != int:
            raise TypeError('Denominator must be integers')

        if self.den == 0:  #is it needed??? (in division ofc, but generally?)
            raise ValueError("Denominator cannot be 0, change te value")





    def __add__(self,other_frac):
        united_num= self.num*other_frac.den + other_frac.num*self.den
        united_den = self.den* other_frac.den
        return Fraction(united_num,united_den)


    def __sub__(self, other_frac):
        united_num = self.num * other_frac.den - other_frac.num * self.den
        united_den = self.den * other_frac.den
        return Fraction(united_num, united_den)

    def __mul__(self, other_frac):
        united_num = self.num * other_frac.num
        united_den = self.den * other_frac.den
        return Fraction(united_num,united_den)

    def __truediv__(self,other_frac):
        united_num = self.num * other_frac.den
        united_den = self.den * other_frac.num
        return Fraction(united_num, united_den)

#overload of operators

    def __lt__(self, other_frac): # <
        if self.den > 0:
            first_num = (-1)*self.num * other_frac.den
            second_num = other_frac.num * (-1)*self.den
            return first_num < second_num
        elif other_frac.den > 0:
            first_num = self.num * (-1)*other_frac.den
            second_num = (-1)*other_frac.num * self.den
            return first_num < second_num
        else:
            first_num= self.num * other_frac.den
            second_num = other_frac.num*self.den
            return first_num < second_num

    def __le__(self,other_frac): # <=
        if self.den > 0:
            first_num = (-1) * self.num * other_frac.den
            second_num = other_frac.num * (-1) * self.den
            return first_num <= second_num
        elif other_frac.den > 0:
            first_num = self.num * (-1) * other_frac.den
            second_num = (-1) * other_frac.num * self.den
            return first_num <= second_num
        else:
            first_num = self.num * other_frac.den
            second_num = other_frac.num * self.den
            return first_num <= second_num

    def __eq__(self,other_frac): # ==
        first_num = self.num * other_frac.den
        second_num = other_frac.num * self.den
        return first_num == second_num

    def __ne__(self,other_frac):# !=
        first_num = self.num * other_frac.den
        second_num = other_frac.num * self.den
        return first_num != second_num

    def __ge__(self,other_frac): # >=
        if self.den > 0:
            first_num = (-1) * self.num * other_frac.den
            second_num = other_frac.num * (-1) * self.den
            return first_num >= second_num
        elif other_frac.den > 0:
            first_num = self.num * (-1) * other_frac.den
            second_num = (-1) * other_frac.num * self.den
            return first_num >= second_num
        else:
            first_num = self.num * other_frac.den
            second_num = other_frac.num * self.den
            return first_num >= second_num

    def __gt__(self,other_frac): # >
        if self.den > 0:
            first_num = (-1) * self.num * other_frac.den
            second_num = other_frac.num * (-1) * self.den
            return first_num > second_num
        elif other_frac.den > 0:
            first_num = self.num * (-1) * other_frac.den
            second_num = (-1) * other_frac.num * self.den
            return first_num > second_num
        else:
            first_num = self.num * other_frac.den
            second_num = other_frac.num * self.den
            return first_num > second_num

    def __str__(self): #needs testing
        """
        Informal representation of fraction
        :return:
        """
        common = gcd(self.num,self.den)
        return str(self.num//common)+ '/' + str(self.den//common)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den




f1=Fraction(1,2)
f2=Fraction(2,-4)
f3=Fraction(4,10)
f4=Fraction(1,1)
#print(f1+f4)
#print(f1+f2)
#print(f1==f2)
print(f1 >f2) #true
print(f1<f2)  #false
print(f1<=f2) #false
print(f1>=f2) #true
#print(f1-f2)
#print(f1*f2)
#print(f1 / f2)


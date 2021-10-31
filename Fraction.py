#!/usr/bin/env python
# coding: utf-8

# In[8]:


from math import floor


# In[2]:


def gcd(x, y):
    """
    Find greatest common divisor
    """
    while(y):
        x, y = y, x % y
  
    return x


# In[3]:


gcd(80, 100)


# In[54]:


def dec_to_fr(x):
    """
    Convert float to fraction
    """
    integral_val = floor(x)
    fractional_part = x - integral_val

    precision = 10000
    gcd_f = gcd(round(fractional_part * precision), precision)
    
    newdenom = precision // gcd_f
    newnum = round(fractional_part * precision / gcd_f) + (integral_val * newdenom)
    
    return [newnum, newdenom]


# In[55]:


dec_to_fr(1.2)


# In[11]:


dec_to_fr(1.5)


# In[10]:


def change_to_frac(other):
    """
    Usage of function converting float to fracion
    :param other: float number
    :return: fraction
    """
    if isinstance(other, float):
        fr = dec_to_fr(other)
        other = Fraction(fr[0], fr[1])
    return other


# In[59]:


class Fraction:    
    """
    Represent fraction and its operetions
    """
    def __init__(self, num, denom):
        """
        Constructor building the class
        :param num: numerator 
        :param den: denominator
        """
        if denom == 0:
            raise ZeroDivisionError("Dividing by zero is not defined!")
        else:
            if isinstance(num, int) and isinstance(denom, int):
                common = gcd(abs(num), abs(denom))
                
                self.numerator = num // common
                self.denominator = denom // common  
                
            elif isinstance(num, float) and isinstance(denom, int):
                tmp_fr = dec_to_fr(num)
                
                numerator = tmp_fr[0]
                denominator =  tmp_fr[1] * denom
                
                common = gcd(abs(numerator), abs(denominator))
                
                self.numerator = numerator // common
                self.denominator = denominator // common
                
            elif isinstance(num, int) and isinstance(denom, float):
                tmp_fr = dec_to_fr(denom)
                
                numerator = num * tmp_fr[1]
                denominator =  tmp_fr[0]
                
                common = gcd(abs(numerator), abs(denominator))
                
                self.numerator = numerator // common
                self.denominator = denominator // common
                
            elif isinstance(num, float) and isinstance(denom, float):
                tmp_fr_num = dec_to_fr(num)
                tmp_fr_den = dec_to_fr(denom)
                
                numerator = tmp_fr_num[0] * tmp_fr_den[1]
                denominator =  tmp_fr_num[1] * tmp_fr_den[0]
                
                common = gcd(abs(numerator), abs(denominator))
                
                self.numerator = numerator // common
                self.denominator = denominator // common

            else:
                raise ValueError("Numerator and denominator should be an integer or floating point!")
                
            if self.denominator < 0:
                    self.numerator = -1 * self.numerator
                    self.denominator = abs(self.denominator)

        
    def __str__(self):
        """
        Informal representation of the fraction 
        """
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator > self.denominator:
            return str(self.numerator//self.denominator) + " " + str(Fraction(self.numerator%self.denominator, self.denominator))
        else:
            return str(self.numerator)+ "/" +str(self.denominator)
    
    def __add__(self, other):
        """
        Add fraction to number or to the other fraction
        :param other: integer or other fraction
        """
        top = self.numerator * other.denominator + self.denominator * other.numerator
        bottom = self.denominator * other.denominator

        return Fraction(top, bottom)
        
    def __sub__(self, other):
        """
        Substract fraction from other fraction or number
        :param other: integer of other fraction
        """
        top = self.numerator * other.denominator - self.denominator * other.numerator
        bottom = self.denominator * other.denominator

        return Fraction(top, bottom)
    
    def __mul__(self, other):
        """
        Multiply fraction with other fraction or number
        :param other: integer of other fraction
        """
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        
        return Fraction(top, bottom)
    
    def __truediv__(self, other):
        """
        Divide fraction by other fraction or number
        :param other: integer of other fraction
        """
        top = self.numerator * other.denominator
        bottom = self.denominator * other.numerator
        
        return Fraction(top, bottom)
    
    def __lt__(self, other): 
        """
        Overload "<" operator for fractions
        """
        other=change_to_frac(other)
        
        return(self.numerator*other.denominator < other.numerator*self.denominator)

    def __gt__(self, other):
        """
        Overload ">" operator for fractions
        """
        other=change_to_frac(other)
        
        return(self.numerator*other.denominator > other.numerator*self.denominator)

    def __eq__(self, other):
        """
        Overload "==" operator for fractions
        """
        other=change_to_frac(other)
        
        return(self.numerator*other.denominator == other.numerator*self.denominator)

    def __ne__(self, other):
        """
        Overload "!=" operator for fractions
        """
        other=change_to_frac(other)
        
        return(self.numerator*other.denominator != other.numerator*self.denominator)

    def __le__(self, other):
        """
        Overload "<=" operator for fractions
        """
        other=change_to_frac(other)
        
        return(self<other or self==other)

    def __ge__(self, other):
        """
        Overload ">=" operator for fractions
        """
        other=change_to_frac(other)
        
        return(self>other or self==other)
    
    def get_num(self):
        """
        Get numerator from the fraction
        """
        return self.numerator
    
    def get_den(self):
        """
        Get denominator from the fraction
        """
        return self.denominator
    
        


# Tworzenie ułamków

# In[68]:


int_int = Fraction(2,3)
print(int_int)

fl_int = Fraction(1.5, 2)
print(fl_int)

int_fl = Fraction(2, 1.2)
print(int_fl)

fl_fl = Fraction(1.5, 1.5)
print(fl_fl)


# Porównywanie ułamków

# In[75]:


x = Fraction(3, 4)
y = Fraction(1, 6)

print(x, y)

print(x, "<", y, x < y)
print(x, ">", y, x > y)
print(x, "==", y, x == y)
print(x, "!=", y, x != y)
print(x, "<=", y, x <= y)
print(x, ">=", y, x >= y)


# In[20]:


f2 = Fraction(3.5, 4)
f2 < 1.5


# In[80]:


fr=Fraction(1,2)
fr > 1/3


# Ujemny mianownik

# In[26]:


test = Fraction(20, -6)
print(test)


# In[77]:


a = Fraction(1, -2)

print(Fraction.get_num(a))
print(Fraction.get_den(a))


# In[12]:


u3 = Fraction(1, 2)
u4 = Fraction(1, -4)

u3 > u4


# In[11]:


u1 = Fraction(1, -2)
u2 = Fraction(1, -4)

u1 < u2


# Postać nieskracalna

# In[62]:


a = Fraction(2.0, 2)
print(a)


# In[28]:


test2 = Fraction(5, 2)
print(test2)


# In[29]:


test3 = Fraction(1.56, 2)
print(test3)


# In[30]:


test4 = Fraction(2, 10.5)
print(test4)


# In[78]:


test4 = Fraction(2.5, 10.5)
print(test4)


# In[63]:


f = Fraction(1, 2)
f2 = Fraction(2, 4)
same = f + f2
print(same)


# Działania arytmetyczne

# In[65]:


f = Fraction(1, 2)
f2 = Fraction(3, 4)
new = f + f2
print(new)


# In[24]:


f3 = Fraction(1, 2)
f4 = Fraction(3, 4)
new2 = f3 - f4
print(new2)


# In[37]:


f5 = Fraction(1, 2)
f6 = Fraction(3, 4)
new3 = f5 * f6
print(new3)


# In[38]:


f7 = Fraction(1, 2)
f8 = Fraction(3, 4)
new4 = f7 / f8
print(new4)


from utily import gcd, dec_to_fr, change_to_frac 
from math import floor

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
        other=change_to_frac(other)
            
        top = self.numerator * other.denominator + self.denominator * other.numerator
        bottom = self.denominator * other.denominator

        return Fraction(top, bottom)
    
    def __radd__(self,other):
        """
        Add fraction to number or to the other fraction
        :param other: integer or other fraction
        """
        other=change_to_frac(other)
            
        top = self.numerator * other.denominator + self.denominator * other.numerator
        bottom = self.denominator * other.denominator

        return Fraction(top, bottom)
        
    def __sub__(self, other):
        """
        Substract fraction from other fraction or number
        :param other: integer of other fraction
        """        
        other=change_to_frac(other)
        top = self.numerator * other.denominator - self.denominator * other.numerator
        bottom = self.denominator * other.denominator

        return Fraction(top, bottom)
    
    def __rsub__(self, other):
        """
        Substract fraction from other fraction or number
        :param other: integer of other fraction
        """        
        other=change_to_frac(other)
        top = self.numerator * other.denominator - self.denominator * other.numerator
        bottom = self.denominator * other.denominator

        return Fraction(top, bottom)
    
    def __mul__(self, other):
        """
        Multiply fraction with other fraction or number
        :param other: integer of other fraction
        """
        other=change_to_frac(other)
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        
        return Fraction(top, bottom)
    
    def __rmul__(self, other):
        """
        Multiply fraction with other fraction or number
        :param other: integer of other fraction
        """
        other=change_to_frac(other)
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        
        return Fraction(top, bottom)
    
    def __truediv__(self, other):
        """
        Divide fraction by other fraction or number
        :param other: integer of other fraction
        """
        other=change_to_frac(other)
        top = self.numerator * other.denominator
        bottom = self.denominator * other.numerator
        
        return Fraction(top, bottom)
    
    def __rtruediv__(self, other):
        """
        Divide fraction by other fraction or number
        :param other: integer of other fraction
        """
        other=change_to_frac(other)
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

fl_fl = Fraction(1.5, 1.5)
print(fl_fl)

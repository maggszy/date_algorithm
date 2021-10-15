def gcd(x,y):
    """
    Find greatest common divisor
    """
    while(y):
        x,y = y, x % y
    return x

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

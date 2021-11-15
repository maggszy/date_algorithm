def power(base, power):
    """
    Calculate the power using exponentiation by squaring
    :param base: number which exponentiation is calculated
    :param power: exponent of the function
    :return: Number raised to the power
    """

    if power < 0:
        raise ValueError("Invalid value")
        
    if not isinstance(power, int):
        raise TypeError("Power should be an integer.")
        
    if power == 0:
        return 1
    
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base)

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base)

    return result

def probability(n, k, p):
    """
    Calculate the Binomial Distribution of k successed in n trials with p probability of success.
    
    :param n: amount of trials
    :param k: amount of successes
    :param p: probability of success
    :return: tuple with wanted probability and number of executed multiplications
    """
    
    if p < 0 or p >1:
        raise ValueError("Probability has a value between 0 and 1")
    
    x=p/(1-p) 
    
    prob=1
    binom_all_x=n*x #for i=1
    count_mult=2 #one multiplication done in x and one in binom_all_x
    
    for i in range(2,k+1):
        binom_all_x*=(n+1-i)/i*x #3 mult
        prob+=binom_all_x
        count_mult+=3
    
    factor = power(1-p,n)
    prob *= factor
    count_mult+=1 #1 mult done in return
    
    return (prob, count_mult)
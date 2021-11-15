def power(base, power):
    MOD = 1000000007

    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result

def probability(n, k, p):
    x=p/(1-p) 
    
    prob=1
    binom_all_x=n*x
    count_mult=2
    
    for i in range(2,k+1):
        binom_all_x*=(n+1-i)/i*x
        prob+=binom_all_x
        count_mult+=3
    
    factor = power(1-p,n)
    prob *= factor
    count_mult+=1
    return (prob, count_mult)

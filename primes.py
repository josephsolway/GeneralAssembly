#primes.py
#Created: Joseph Solway June 19 2014
#Reference code by Stefan @ http://stackoverflow.com/a/22808285/ 

def primes(n):
    i = 2
    factors = []
    while i * i <= n: #while i is less than the maximum value of a possible prime
        if n % i: #if n is not divisble by i then increase i by 1
            i += 1
        else: #else if n is divisible by i, then n = n / i
            n //= i 
            factors.append(i) #add the factor i to the list of factors
    if n > 1: 
        factors.append(n)
    return factors
    
# primes(600851475143)
# [71, 839, 1471, 6857L]
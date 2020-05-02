from math import factorial
from collections import Counter
from math import gcd

def cycles_counted(c, n):
    c_c = factorial(n)
    for a, b in Counter(c).items():
        c_c //= (a ** b) * factorial(b)
    return c_c        

def cycles_partitioned(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in cycles_partitioned(n-i, i):
            yield [i] + p

def answer(w, h, s):    
    res = 0
    for wid in cycles_partitioned(w):
        for hei in cycles_partitioned(h):            
            m = cycles_counted(wid, w) * cycles_counted(hei, h)
            res +=m *(s**sum([sum([gcd(i, j) for i in wid]) for j in hei]))
              
    return str(res // (factorial(w) * factorial(h)))


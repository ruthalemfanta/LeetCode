from math import gcd
from functools import reduce
from itertools import combinations
def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def main():
    k = int(input(""))
    l = int(input(""))
    m = int(input(""))
    n = int(input(""))
    d = int(input(""))
    
    divisors = [k, l, m, n]
    damaged = 0

    for i in range(1, len(divisors) + 1):  
        for comb in combinations(divisors, i):  
            lcm_val = lcm_multiple(comb)
            if i % 2 == 1: 
                damaged += d // lcm_val
            else:  
                damaged -= d // lcm_val

    print(damaged)

if __name__ == "__main__":
    main()

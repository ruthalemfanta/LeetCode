from math import gcd

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    return str1[:gcd(len(str1), len(str2))]



str1 = 'ABAB'
str2 = 'ABABAB'

print(gcdOfStrings(str1, str2)) 
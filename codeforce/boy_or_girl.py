def test():
    s = list(input())
    distinct = set(s)
    if len(distinct) % 2 != 0:
        print('IGNORE HIM!')
    else:
        print('CHAT WITH HER!')

test()
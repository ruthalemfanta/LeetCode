from collections import defaultdict

def football():
    n = int(input())  
    m = defaultdict(int)  

    for _ in range(n):
        s = input().strip()  
        m[s] += 1  

    max_count = -float('inf')  
    ans = ""

    for key, value in m.items():
        if max_count < value:  
            max_count = value
            ans = key

    print(ans)  

if __name__ == "__main__":
    football()

def stringTask(input):
    vowels = set('aeiouy')  
    result = []
    for i in input:
        if i.lower() not in vowels:  
            result.append('.' + i.lower())  

    return ''.join(result)

input_str = input().strip()  
print(stringTask(input_str))  

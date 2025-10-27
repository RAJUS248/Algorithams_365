def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num-1) 

# print(factorial(2))

def factorial_v2(num):
    result = 1
    for i in range(2,num+1):
        result *= i

        
    return result

print(factorial_v2(100))
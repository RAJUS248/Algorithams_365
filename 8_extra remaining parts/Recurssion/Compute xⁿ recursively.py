def power(x,n):
    if n == 0:
        return 1
    
    return x ** n

print(power(2,2))

# or

def power_v2(x,n):
    if n == 0:
        return 1
    
    return x * power(x,n-1)

print(power_v2(2,2))

def isEven(number:int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
    
result = isEven(25)

if result:
    print("is even number")
else:
    print("is odd number")
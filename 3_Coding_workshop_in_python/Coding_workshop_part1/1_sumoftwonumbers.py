def getSum(number1, number2):
    return number1 + number2

#invocation/call he function 
#polymorphisum : one function work for different data types
sum = getSum(24,28)
print("sum of two numbers is",sum)

sum2 = getSum(2.5,2.6)
print("sum of two numbers is",sum2)

sum3 = getSum("hello"," raju")
print("sum of two numbers is",sum3)


# using return type -> int
def getIntegerSum(number1:int , number2:int) -> int:
    answer = number1 + number2 
    return answer

sumint = getIntegerSum(1.2,2.4)
print("sum of two numbers is", sumint)

sumint1 = getIntegerSum(100,2.4)
print("sum of two numbers is", sumint1)
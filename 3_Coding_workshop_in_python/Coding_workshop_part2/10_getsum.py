#without range function
def getSum(numbers:list)-> int:

    sum = 0

    for number in numbers:
        sum += number

    return sum

numbers = [1,2,3]
sumOfNumbers = getSum(numbers)
print(f"sum of numbers = {sumOfNumbers}")


#with range function

def getSum1(numbers1:list)-> int:
    sum1 = 0

    length = len(numbers1)

    for index in range(0, length, 1):
        sum1 = sum1 + numbers1[index]
    
    return sum1

numbers1 = [1,2,3,4]
sumOfNumbers1 = getSum1(numbers1)
print(f"sum of numbers = {sumOfNumbers1}")
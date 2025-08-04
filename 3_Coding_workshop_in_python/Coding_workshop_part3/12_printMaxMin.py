# def getMaxMin(numbers:list)-> tuple[int,int]:
def getMaxMin(numbers:list):
    max = numbers[0]
    min = numbers[0]
    
    number = len(numbers)
    for index in range(1,number,1):
        if numbers[index] > max:
            max = numbers[index]

        if numbers[index] < min:
            min = numbers[index]

        
    
    return max,min

input1 = [0,2,113,4]

resultMax, resultMin = getMaxMin(input1)

print(f"max value is {resultMax} and min value {resultMin}")
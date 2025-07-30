def swap(number1:int, number2:int):
    temp = number1
    number1 = number2
    number2 = temp
    return number1,number2

iteam1 = 10
iteam2 = 20

print(f"before : value of iteam1 is {iteam1} and iteam2 is {iteam2}")

iteam1, iteam2 = swap(iteam1 , iteam2)

print(f"after : value of iteam1 is {iteam1} and iteam2 is {iteam2}") 



#simple swap
def swapsimple(item1:int,item2:int):
    
    return item2,item1

number1 = 10
number2 = 20

print(f"before : value of number1 is {number1} and number2 is {number2}")

number1, number2 = swapsimple(number1 , number2)
print(f"after : value of number1 is {number1} and number2 is {number2}") 

#for not using extra memory

def isPalindrome(string:str)->bool:
    leftIndex = 0
    rightIndex = len(string) - 1
    result = True

    while (leftIndex < rightIndex):
        if string [leftIndex] != string[rightIndex]:
            result = False
            break

        leftIndex += 1
        rightIndex -= 1

    return result 

input1 = "mom"
input2 = "malayalam"
input3 = "hello"
input4 = "abba"

result = isPalindrome(input4)

if result:
    print("is palindrome")

else:
    print("not palindrome")
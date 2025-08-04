#

def search(number,key):
    leftIndex = 0
    rightIndex = len(number) - 1
    found = False

    while(leftIndex <= rightIndex):
        middleIndex = int(leftIndex + ( rightIndex - leftIndex /2 ))

        if (number[middleIndex] == key):
            found = True
            break

        if(number[middleIndex] > key):

            rightIndex = middleIndex -1

        else:
            leftIndex = middleIndex + 1

    return found

input1 = [1,2,3,4,5,6,7]
key = 7

result = search(input1,key)

if result:
    print("number is found")

else:
    print("number is not found")
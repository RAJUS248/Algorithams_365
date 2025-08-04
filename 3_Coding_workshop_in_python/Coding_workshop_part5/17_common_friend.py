def getCommonelment(input1 , input2):

    for input1_index in range(0,len(input1),1):
        isFound = False

        for input2_index in range(0, len(input2),1):

            if input1[input1_index] == input2[input2_index]:
                isFound = True
                break

        if isFound:
            print(input1[input1_index])

input1 = [1,2,3,4,1]
input2 = [3,2,5,8,9,1]

getCommonelment(input1,input2)
        
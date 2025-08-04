def print_Unique_Number(numbers):

    for read_index in range (0 , len(numbers),1):
        isDublicate = False

        for compair_index in range(0,len(numbers),1):
            if read_index == compair_index:
                continue

            elif numbers[read_index] == numbers[compair_index]:
                 isDublicate = True
                 break
            
        if isDublicate == False:
            print(numbers[read_index]) #this the the unique element hence print it

numbers = [1,4,5,4]
print_Unique_Number(numbers)




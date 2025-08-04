# only for counting bits in number

def printBinaryForm1(number:int):

    no_of_bits = number.bit_length()

    print(f"Number of bits {no_of_bits}")

printBinaryForm1(10)

#for counting bits and also in binary form of number

def printBinaryForm(number:int):

    no_of_bits = number.bit_length()

    print(f"Number of bits {no_of_bits}")

    mask = 1
    mask = mask << no_of_bits # left bitwise oprator

    for _ in range(no_of_bits):
        if number & mask:
            print("1", end ="") # end ="" this is for printing numbers in one after the number --> 1 0 0 0 0
        else:
            print("0", end ="")

        mask = mask >> 1  # right shift bitwise oprator
printBinaryForm(1024)
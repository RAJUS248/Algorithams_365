def str_length(string):
    counter = 0
    for character in string:
        counter += 1

    return counter

input = "None" #None -> null    but running "None"
print(f"string length of {input} is {str_length(input)}")

input2 = ""
print(f"string length of {input2} is {str_length(input2)}")

input3 = "R"
print(f"string length of {input3} is {str_length(input3)}")

input4 = "raja"
print(f"string length of {input4} is {str_length(input4)}")

# new for NOne  IMPORTENT

def str_length2(string2):
    counter = 0
    if string2 != None:
        for character2 in string2:
            counter += 1

    return counter

input = None
print(f"string length of {input} is {str_length2(input)}")

input2 = ""
print(f"string length of {input2} is {str_length2(input2)}")

input3 = "R"
print(f"string length of {input3} is {str_length2(input3)}")

input4 = "raja"
print(f"string length of {input4} is {str_length2(input4)}")
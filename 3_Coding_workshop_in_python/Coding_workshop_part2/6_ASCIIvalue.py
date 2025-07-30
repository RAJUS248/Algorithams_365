def printASCIIofString(string):
    for character in string:
        print(f"{character} ->{ord(character)}") #ord is ASCII value finder

printASCIIofString("raj")        


def printASCIIofString2(string2):
    for character2 in string2:
        ASCII_value = ord(character2)
        print(f"{character2} ->{ASCII_value}") #ord is ASCII value finder

printASCIIofString("abc") 
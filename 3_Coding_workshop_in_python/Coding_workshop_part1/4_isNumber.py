def isNumber(number):
    isInteger = True

    for eachCharacter in number:
        if eachCharacter >= '0' and eachCharacter <= '9' :
            continue
        else:
            isInteger = False
            break
    return isInteger
result = isNumber("123B") 

if result:
    print("yes it is an integer")

else:
    print(" it is not an integer")


#simple way

def isNumber2(number2):
    # check if any of the character falls outside the range o to 9, if yes return false
    for eachchar in number2:
        if eachchar < '0' or eachchar > '9' :

            return False
    # all the characters are between 0 to 9 hence return true
    return True

result2 = isNumber2("12a3B") 

if result2:
    
    print("yes it is an integer")

else:
    print(" it is not an integer")
# it only count the space not word there is bug in code

def getWordCount(String):
    counter = 0

    for char in String:
        if char == ' ' or char == '\t' or char == '\n':
            counter +=1

    # spacial case with just one word 

    if (len(String) > 0 and counter == 0):
        
        return 1
    
    return counter

String = ""

result = getWordCount(String)

print(result)

# there will be no word or atleast one word in the input but not work for spaces

def getWordCount1(String):
    counter = 1

    if len(String) == 0 :
        return 0

    for char in String:
        if char == ' ' or char == '\t' or char == '\n':
            counter +=1
    
    return counter

String = " "

result = getWordCount1(String)

print(result)



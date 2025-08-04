def removeSpaceString(string):
    output = ''

    for character in string:
        if character != ' ' and character != '\t' and character != '\n' :
            output = output + character

    print(output)

input = "a"
removeSpaceString(input)
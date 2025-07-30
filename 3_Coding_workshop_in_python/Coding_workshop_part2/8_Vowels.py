def count_vowels(string)-> int:
    counter = 0
    if string != None:
        for character in string:
            if (character == 'a' or
                character == 'e' or
                character == 'i' or
                character == 'o' or
                character == 'u' or
                character == 'A' or
                character == 'E' or
                character == 'I' or
                character == 'O' or
                character == 'U' ):

                counter +=1

    return counter
input = None
print(f"number of vowels in {input} is = {count_vowels(input)}  ")

input = "raja"
print(f"number of vowels in {input} is = {count_vowels(input)}  ")

input = "123"
print(f"number of vowels in {input} is = {count_vowels(input)}  ")
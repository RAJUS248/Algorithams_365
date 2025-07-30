""" def revers_string(string):
    length = len(string)
    middle = int(length / 2)
    print(f"lenth = {length}")
    print(f"middle = {middle}")
    print("loop 1")
    for start in range(0, length, 1):
        print(start)

    print("loop 2")
    for end in range (length-1,-1,-1):
        print(end)
# u can zip / merge the for loop 

#   for start, end in zip(range(0 ,length , 1), range(length-1 , -1, -1))

name = "rajaa"
revers_string(name)
print(name)               """
  

def revers_string2(string2):

    length = len(string2)

    revers_string2 = ""
    for end in range (length-1,-1,-1):
        revers_string2 += string2[end]
    return revers_string2

name2 = "rajaa"
name2 = revers_string2(name2)
print(name2)


def reverse_string(name:str):
   
   if len(name) == 0:
       return name
   return reverse_string(name[1:]) + name[0]

name = "Raja"
print(reverse_string(name)) 


text = "hello"
reversed_text = text[::-1]
print(reversed_text)





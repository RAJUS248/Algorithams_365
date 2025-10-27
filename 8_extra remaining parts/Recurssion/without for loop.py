def print_number(num):
    
    # termination
    if num == 0:
        return
    
    # work or logic
    num = num - 1
    print(num)

    # recurssion call
    print_number(num) 
    print(num)

print_number(5)

def print_number_v2(num):
    
    # termination
    if num == 0:
        return
    
    # work or logic

    print("befor",num)
    # recurssion call
    print_number_v2(num - 1) 
    print("after",num)

print_number_v2(5)


    


    
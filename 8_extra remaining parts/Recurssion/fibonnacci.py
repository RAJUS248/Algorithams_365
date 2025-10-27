def fibonnacci(num):
    if num <= 1:
        return num
    # print(f"{fibonnacci(num-1)} + {fibonnacci(num-2)} = {fibonnacci(num-1) + fibonnacci(num-2)} ")
    return fibonnacci(num-1) + fibonnacci(num-2)
     

print(fibonnacci(7))

# 📌 Expansion of fibonnacci(7)
#
# fibonnacci(7)
# = fibonnacci(6) + fibonnacci(5)
#
# Expand fibonnacci(6)
# fibonnacci(6)
# = fibonnacci(5) + fibonnacci(4)
#
# Expand fibonnacci(5)
# fibonnacci(5)
# = fibonnacci(4) + fibonnacci(3)
#
# Expand fibonnacci(4)
# fibonnacci(4)
# = fibonnacci(3) + fibonnacci(2)
#
# Expand fibonnacci(3)
# fibonnacci(3)
# = fibonnacci(2) + fibonnacci(1)
#
# Expand fibonnacci(2)
# fibonnacci(2)
# = fibonnacci(1) + fibonnacci(0)
# = 1 + 0 = 1
#
# ✅ Now substitute back results
#
# fibonnacci(2) = 1
# fibonnacci(3) = fibonnacci(2) + fibonnacci(1) = 1 + 1 = 2
# fibonnacci(4) = fibonnacci(3) + fibonnacci(2) = 2 + 1 = 3
# fibonnacci(5) = fibonnacci(4) + fibonnacci(3) = 3 + 2 = 5
# fibonnacci(6) = fibonnacci(5) + fibonnacci(4) = 5 + 3 = 8
# fibonnacci(7) = fibonnacci(6) + fibonnacci(5) = 8 + 5 = 13
#
# Final Answer: 13


def fibonnacci_v2(num):

    if num <= 1:
        return num
    
    num1 = fibonnacci_v2(num - 1)
    num2 = fibonnacci_v2(num - 2)
    
    ans = num1 + num2
    # print(f"{num1} + {num2} = {ans}")
    
    return ans


print(fibonnacci_v2(2))

def fibonnacci_v3(num):

    if num <= 1:
        return num
    
    a,b = 0,1
    for _ in range(2,num+1):
        a,b = b, a+b

    return b

print(fibonnacci_v3(20577))

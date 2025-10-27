def sum_of_num(num):
    if num == 0:
        return 0
    return num + sum_of_num(num - 1)

print(sum_of_num(5))
numbers = [1, 4, 9, 11, 5]

numbers.append(6)
numbers.append(7)
numbers.append(12)

print(numbers)

numbers.sort()
print(numbers)

numbers.insert(2, 8)
print(numbers)

numbers.remove(4)
print(numbers)

numbers.reverse()
print(numbers)

value = numbers.pop()
print(value)
print(numbers)

for number in numbers:
    print(number)

print(numbers[3])


# 2D

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix)

matrix[0][1] = 10
print(matrix)

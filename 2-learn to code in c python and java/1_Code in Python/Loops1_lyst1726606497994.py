# for loop normal counting starting from 0 to 9
for i in range(10):
    print(i)

# item in values
values = range(10)
for item in values:
    print(item)


#  for loop(start, stop, step) for reverse counting
for index in range(10, 0, -1):
    print(index)

# for loop(start, stop, step) for 1 + 2 = 3, 3+2 = 5, 5+2 = 7, etc.
for index in range(1, 10, 2):
    print(index)

# for name in names also prints the name in uppercase
names = ["Raju", "Ram", "Rajat", "Rani", "Rita"]

for name in names:
    print(name)
    print(name.upper())


# counting using while loop
count = 0
while(count <= 10):
    print(count)
    count = count+1

# Neasted for loop Print the multiplication table from 2 to 10 
for i in range(2,4):
    print(f"Multiplication table for {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")


# breaking out of the loop 
for number in range(10):
    if number == 5:
        print("Breaking out of the loop at number 5")
        break
    print(number)

# skipping an iteration with continue
names = ["Raju", "Ram", "Rajat", "Rani", "Rita"]
for name in names:
    if name == "Ram":
        continue
    print(name)


# using list comprehensions (one - liner for loop)
squares = [number ** 2 for number in range(6)]
print(squares)


#for loop with else
for number in range(5):
    print(number)
else:
    print("number runs without break")


#for loop with else with break
for number in range(5):
    print(number)
    if number == 3:
        print("3 is found so break")
        break
else:
    print("number runs without break")

#for loop with else with break with list
numbers = [1,2,3,4,5,6,]
for number in numbers:
    print(number)
    if number == 3:
        print("3 is found so break")
        break
else:
    print("3 is not found")
# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
x,y,z = fruits
print(x)
print(y)
print(z)

# Using Asterisk*
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
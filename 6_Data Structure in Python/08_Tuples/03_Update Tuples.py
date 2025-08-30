# Change Tuple Values
# Convert the tuple into a list to be able to change it:
tuple1 = ("apple", "banana", "cherry")
Update_tuple = list(tuple1)
Update_tuple[1] = "kiwi"
tuple1 = tuple(Update_tuple)
print(tuple1)

# Add Items
Update_tuple.append("orange")
tuple1 = tuple(Update_tuple)
print(tuple1)

# . Add tuple to a tuple.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Remove Items
Update_tuple.remove("apple")
tuple1 = tuple(Update_tuple)
print(tuple1)

# The del keyword can delete the tuple completely:
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

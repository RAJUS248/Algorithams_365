# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
print(thistuple[2:])

# Range of Negative Indexes
print(thistuple[-4:-1])

# Check if Item Exists
if "apple" in thistuple:
    print("yes")
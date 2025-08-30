from Main import Fruits

thisset = Fruits.thisset

# first printing all names of fruits 
print("All names of fruits ")
print(thisset ,"\n")


# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")   # only remove not return 
thisset.discard("cherry")

# The return value of the pop() method is the removed item.
# Remove a random item by using the pop() method:
x = thisset.pop()
print("the pop item is:",x)

print(thisset)

# The clear() method empties the set:
thisset.clear()

print(thisset)

# The del keyword will delete the set completely:
del thisset
print(thisset)   # #this will raise an error because the set no longer exists
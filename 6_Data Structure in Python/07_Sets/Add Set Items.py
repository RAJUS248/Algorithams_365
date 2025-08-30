from Main import Fruits

thisset = Fruits.thisset

# first printing all names of fruits 
print("All names of fruits ")
print(thisset ,"\n")


# Add an item to a set, using the add() method:
thisset.add("orange")
print(thisset)

# To add items from another set into the current set,
#  use the update() method.

some_more_fruits = {"pineapple", "mango", "papaya"}

thisset.update(some_more_fruits)
print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).

mylist = ["kiwi","sitaphal"]

thisset.update(mylist)

print(thisset)

# copy 
set1 = {"a", "b", "c"}
set1.copy()
print(set1)
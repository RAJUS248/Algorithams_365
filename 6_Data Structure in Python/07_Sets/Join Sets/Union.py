set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

print("\n the Union mthd \n")
# Union
# The union() method returns a new set with all items from both sets.
# The union() and update() methods joins all items from both sets.
join_set = set1.union(set2)
print(join_set)

# You can use the | operator instead of the union()
# Note: The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the  union() method.
join_set = set1 | set2
print(join_set) 

# Join Multiple Sets
# Join multiple sets with the union() method
myset = set1.union(set2,set3,set4)
print(myset)

# When using the | operator, separate the sets with more | operators:
myset = set1 | set2 | set3 |set4
print(myset)

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z, "\n")

# Update
print("the Update mthd \n")
# The update() method inserts the items in set2 into set1:
# Note: Both union() and update() will exclude any duplicate items.
set1.update(set2)
print(set1)





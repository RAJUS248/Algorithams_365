# Difference
print("the Difference mthd \n")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# The difference() method will return a new set 
# that will contain only the items from the first set 
# that are not present in the other set.
set3 = set1.difference(set2)
print(set3)                    # o/p -> {'cherry', 'banana'}


# You can use the - operator instead of the difference() method, 
# and you will get the same result.
set3 = set1 - set2
print(set3)

# Note: The - operator only allows you to join sets with sets, 
# and not with other data types like you can with the difference() method.

# The difference_update() method will also keep the items 
# from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.

set1.difference_update(set2)
print(set1)

# Symmetric Differences
print("\n the Symmetric Difference mthd \n")

# The symmetric_difference() method will keep only 
# the elements that are NOT present in both sets.

set10 = {"apple", "banana", "cherry"}
set20 = {"google", "microsoft", "apple"}

set4 = set10.symmetric_difference(set20)
print(set4)

# You can use the ^ operator 
# instead of the symmetric_difference() method
# The ^ operator only allows you to join sets with sets,
set4 = set10 ^ set20
print(set4)

# The symmetric_difference_update() method will also 
# keep all but the duplicates, 
# but it will change the original set instead of returning a new set.

set10.symmetric_difference_update(set20)
print(set10)
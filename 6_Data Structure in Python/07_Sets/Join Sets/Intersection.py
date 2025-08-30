# Intersection
print("the Intersection mthd \n")

# Keep ONLY the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, 
# and you will get the same result.
# Note The & operator only allows you to join sets with sets, 
# and not with other data types like you can with the intersection() method.
set4 = set1 & set2
print(set4)

# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1)

# The values True and 1 are considered the same value. 
# The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set4 = set1.intersection(set2)
print(set4)

#  will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1)


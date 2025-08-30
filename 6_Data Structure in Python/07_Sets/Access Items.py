from Main import Fruits

# thisset = {"apple", "banana", "cherry"} 
# or import and write this 
thisset = Fruits.thisset

# first printing all names of fruits 
print("All names of fruits ")
print(thisset ,"\n")

# Loop Sets  
# Loop through the set, and print the values:
for x in thisset:
    print(x)


# Check if "banana" is present in the set:
print("banana" in thisset)


# Check if "banana" is NOT present in the set:
print("banana" not in thisset)
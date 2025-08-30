thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# There is also a method called get()
# that will give you the same result:
x = thisdict.get("model")
print(x)

# Get Keys
x = thisdict.keys()
print(x)

# Add a new item to the original dictionary,
thisdict["color"] = "white"
print(x)

# Get Values
x = thisdict.values()
print(x)

# Make a change in the original dictionary, 
thisdict["year"] = 2025
print(x)

# Add a new item to the original dictionary,
thisdict["color"] = "red"
print(x)

# Get Items
x = thisdict.items()
print(x)

# Check if Key Exists
if "model" in thisdict:
    print("yes")
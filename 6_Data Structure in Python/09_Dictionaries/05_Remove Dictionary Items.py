# The pop()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
del thisdict["brand"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
del thisdict
print(thisdict)

# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)
myfamily = {
    "child1" :{
        "name": "rashti",
        "year": 2028
    },
    "child2" :{
        "name": "sruja",
        "year": 2029
    },
    "child3" :{
        "name": "rashi",
        "year": 2030
    }
}
print(myfamily)

# OR

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1 = {
    "child1": child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily1)

# Access Items in Nested Dictionaries
print(myfamily["child1"]["name"])

# Loop Through Nested Dictionaries
# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
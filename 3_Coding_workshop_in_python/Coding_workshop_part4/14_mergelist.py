def mergeList(list1:list,list2:list)-> list:

    for item in list2:
        list1.append(item)

    

list1 = [1,2,3]
list2 = [14,5]

mergeList(list1,list2)

print(f"the list1 = {list1}")

#my own
def listmerge(list1,list2):
    return list1 + list2

list1 = [1,2,3]
list2 = [4,5]

result = listmerge(list1,list2)
print("list merge is =",result)
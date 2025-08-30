class Sets:

    myset = {"apple","banana","cherry"}
    print(myset)

    # Duplicate values will be ignored:
    thisset = {"apple", "banana", "cherry", "apple"}
    print(thisset)

    # True and 1 is considered the same value:
    thisset2 = {"apple", "banana", "cherry", True, 1, 2}
    print(thisset2)

    # False and 0 is considered the same value:
    thisset3 = {"apple", "banana", "cherry", False, True, 0}
    print(thisset3)

    # Get the number of items in a set:
    print(len(thisset3))

    # String, int and boolean data types:
    set1 = {"apple", "banana", "cherry"}
    set2 = {1, 5, 7, 9, 3}
    set3 = {True, False, False}

    print(set1)
    print(set2)
    print(set3)

    # A set with strings, integers and boolean values:
    set1 = {"abc", 34, True, 40, "male"}
    print(set1)

    # type()
    myset = {"apple", "banana", "cherry"}
    print(type(myset))

    # Using the set() constructor to make a set:

    thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
    print(thisset)
class person:

    def __init__(myObject , name,age):  # self --> myObject   # self parameter

        myObject.name = name
        myObject.age = age

    def myfun(abc):

        print("my name is " + abc.name)

p1 = person("raja" , 22)

p1.myfun()
        
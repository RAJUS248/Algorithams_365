class Persion:
    def __init__(self,name,age):

        self.name = name
        self.age = age

    def myfun(self):

        print ("my name is "+ self.name, "and age is", self.age)

p1 = Persion("raja",22)
p1.myfun()        
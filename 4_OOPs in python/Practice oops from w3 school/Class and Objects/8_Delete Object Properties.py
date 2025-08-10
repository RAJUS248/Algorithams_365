class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name , self.age)

p1 = Person("John", 36)

del p1.age                 #deleteing the object property like age 

print(p1.age)
p1.myfunc()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + p1.name)

p1 = Person("John", 36)

p1.age = 40
p1.name = "raj"

print(p1.age)
print(p1.name)

p1.myfunc()
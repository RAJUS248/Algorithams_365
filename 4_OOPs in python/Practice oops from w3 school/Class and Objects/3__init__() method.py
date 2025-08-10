class Persion:

    def __init__(self,Name,Age):

        self.name = Name
        self.age = Age

p1 = Persion ("raja" , 22)

print(p1.name)  # only take self.name  not take Name 
print(p1.age)  # only take self.age     not take Age
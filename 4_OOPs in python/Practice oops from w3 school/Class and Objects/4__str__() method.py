class Person:

    def __init__(self,Name,Age):

        self.Name = Name
        self.Age = Age

    def __str__(self):
        
        return f"{self.Name} ({self.Age})"
    
p1 = Person("Raja",22)
print(p1)


        
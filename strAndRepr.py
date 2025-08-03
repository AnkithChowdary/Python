class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"Name: {self.name} age:{self.age}"
    #It is normally used in python debugger
    # Used to recreate the object from the string representation
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob=Person("Bob",35)
print(bob)

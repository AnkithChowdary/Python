# student={"name":"Rolf","grades":(89,90,93,78,90)}

# def average(sequence):
#     return sum(sequence)/len(sequence)

# print(average(student["grades"]))

class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def average(self):
        return sum(self.grades)/len(self.grades)



student=Student("Bob",(90,100,93,78,97))
student2=Student("Rolf",(94,100,93,92,94))
print(student.name)
print(student.average())

print(student2.name)
print(student2.average())

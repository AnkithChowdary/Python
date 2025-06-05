t=5,11 # This is a tuple with two elements
print(t)
# Destructuring variables   
x,y=t

print(x, y) 

student_attendance={"Rolf":96,"Bob":80,"Anne":100}

print(list(student_attendance.items())) ## Convert dictionary items to a list of tuples
# Destructuring dictionary items

for t in student_attendance.items():
    print(t)

people=[("Bob",42,"Mechanic"),("Anne",36,"Engineer"),("Suresh",28,"Doctor")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person=("Bob",42,"Mechanic")
name,_,profession=person

print(name, profession)

*head,tail=[1,2,3,4,5]

print(head)
print(tail)


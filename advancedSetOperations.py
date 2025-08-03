# Union
studentA={"Football","Cricket","Coding"};
studentB={"Binge Watching","Cricket","Basketball"};
# Total hobbies
print(studentA.union(studentB))

# Hobbies of only StudentA 
print("Hobbies of only StudentA: ",studentA.difference(studentB))

print("Common hobbies: ",studentA.intersection(studentB))


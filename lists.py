def print_list(li):
  for num in li:
    print(num,end=" ")


print("Hello world")

li=[1,2,3,4,5,6]
# Step of 3
print(li[::3])
# Printing the list
print_list(li)
print();
# Slicing
sub=li[2:4]
print_list(sub)
print()
# To append an element in the list
sub.append(5);
print_list(sub)
print()
# Removing element from the list
sub.remove(4);
print_list(sub)
print()
# Inserting element in the list
sub.insert(0,7)

print_list(sub)
print()

# Reverse List
sub.reverse()
print_list(sub)
print()

#copy list
li2=li.copy()
print(li2)
sub.sort()
print(sub)
sub.append(5);

print(sub.count(5))
print(sub.index(5))


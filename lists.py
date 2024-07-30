def print_list(li):
  for num in li:
    print(num,end=" ")




li=[1,2,3,4,5,6]
print(li[::3])
print_list(li)
print();
sub=li[2:4]
print_list(sub)
print()
sub.append(5);
print_list(sub)


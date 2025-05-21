# Tuples: immutable, ordered, allows duplicate elements  no insert, remove, pop, clear
t=(1,2,3,4,5);
# Lists: mutable, ordered, allows duplicate elements
l=[1,2,3,4,5];
# Sets: mutable, unordered, no duplicate elements
s={1,2,3,4,5};

print(t);
l.append(6);
print(l);
l.remove(6);
l.reverse();
print(l);
l.insert(1,6);
print(l);
l.pop();
print(l);
l.clear();
print(l);
s.add(6);
print(s);
s.remove(6);
print(s);
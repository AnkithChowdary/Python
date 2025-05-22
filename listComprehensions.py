numbers=[1,3,5]
doubled=[num*2 for num in numbers]

for num in doubled:
  print(num)

friends=["Suresh","Karan","Saurabh","Saint"]
s_friend=[]
for friend in friends:
  if friend.startswith("S"):
    s_friend.append(friend)

friends_2=[]

for friend in friends:
  friends_2.append(friend)


print(s_friend)

print(friends is friends_2)
print("friends: ",id(friends)," friends2:",id(friends_2))



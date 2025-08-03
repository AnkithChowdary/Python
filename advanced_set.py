friends={"Bob", "Rolf", "Anne"}
abroad={"Bob", "Anne"}

local_friends=abroad.difference(friends)

print(local_friends)


all_friend=abroad.union(friends);
print(all_friend)


common_friends=abroad.intersection(friends)
print(common_friends)

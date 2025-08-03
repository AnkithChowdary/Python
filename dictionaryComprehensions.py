users=[
  (0,"Bob","password"),
  (1,"Rolf","Bob123"),
  (2,"Jose","longp4assword"),
  (3,"username","1234")
]
# With the user as key the whole tuple is mapped
username_mapping={user[1]:user for user in users} 

print(username_mapping)


username_input=input("Enter your username: ")
password_input=input("Enter your password: ")

_,username,password=username_mapping[username_input]

if password_input==password:
    print("your details are correct!")
else:
    print("Your details are incorrect")
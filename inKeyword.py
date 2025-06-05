movies={"Avenger end game","Three idiots","KGF"}
user_movie=input("Enter the movie name : ")
print(user_movie in movies)



print("Guess the number ")
num=5
user_input=input("Would you like to start?")

if user_input in ["Y", "y"]:
    user_number=int(input("Guess the number:"))
    if user_number==num:
        print("You guess correctly")
    else:
        print("Wrong guess")

mynumber=5
while True:
    user_input=input("Do you want to play (y/n)")
    if user_input=="n":
        break;
    num=int(input("Enter the number : "))
    if num==mynumber:
        print("Yay! your guess is right")
    elif num<mynumber:
        print("Less the secret number")
    else:
        print("More the secret number")

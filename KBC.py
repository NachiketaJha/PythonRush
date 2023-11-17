#A quiz system which credits user a certain amount of money upon guessing correct answers
x = input("Are You Smart Enough to Play KBC? (Yes/No)")
match x:
    case "Yes":
        print("Alright!")
        User = input("Player! Please Enter Your Name:")
    case "yes":
        print("Alright!")
        User = input("Player! Please Enter Your Name:")
    case "YES":
        print("Alright!")
        User = input("Player! Please Enter Your Name:")
    case "No" :
        print("Haha! kiddo just go and read some books.")
    case "no" :
        print("Haha! kiddo just go and read some books.")
    case "NO" :
        print("Haha! kiddo just go and read some books.")
    case _:
        print("STOP MESSING WITH MY CODE :(")


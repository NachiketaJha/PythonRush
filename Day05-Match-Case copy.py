#MatchCase - Matching Variable with all the patterns
User = input("Please Type Your Name!")
print("Welcome Back!", User)
print("Let's Play a Game.")
x = int(input("Guess A Value between 0 to 9"))

match x:
    case 0:
        print("Oh no! You were close:( ")
    case 1:
        print("Oh no! You were close:( ")
    case 2:
        print("Oh no! You were close:( ")
    case 3:
        print("Oh no! You were close:( ")
    case 4:
        print("Oh no! You were close:( ")
    case 5:
        print("Oh no! You were close:( ")
    case 6:
        print("Oh no! You were close:( ")
    case 7:
        print("Bravo! You Guessed it right")
    case 8:
        print("Oh no! You were close:( ")
    case 9:
        print("Oh no! You were close:( ")
    case _:
        print("Invalid Input")

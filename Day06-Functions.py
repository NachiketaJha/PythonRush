#Create functions so we can use it later/ repeat
#instead of writing entire thing again and again

#check which one is greater and find mean

def fmean(a,b):
    mean = (a+b)/2
    print(mean)

def whobig(a,b):
    if(a>b):
        print(a, "is greater than", b)
    else:
        print(b, "is greater than", a)

a = int(input("Enter First Value:"))
b = int(input("Enter Second Value:"))
whobig(a,b)
fmean(a,b)

x = input("You want more ?(Yes/No)")
match x:
    case "YES":
        print("ok! Let's try for these")
    case "Yes":
        print("ok! Let's try for these")
    case "yes":
        print("ok! Let's try for these")
    case "NO":
        print("We, will see you later!")
    case "No":
        print("We, will see you later!")
    case "no":
        print("We, will see you later!")
    case _:
        print("Oh no! Invalid Input")

c = int(input("Enter Third Value:"))
d = int(input("Enter Fourth Value:"))
whobig(c,d)
fmean(c,d)

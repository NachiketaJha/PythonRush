#while loop
# if somebody asks for DO WHILE LOOP - then execute the while loop content one time before loop
Age = int(input("Enter Your Age:"))

while (Age>=18):
    print("You Can Vote!")

if (Age<0):
    print("Pls don't ruin my code💔")

elif(Age<18, Age>0):
    print("Grow a Beard Kid!🤓")

else:
    print("Unexpected Error!")
#Eliff used For adding extra conditions if previous ones get failed
Username = input("Please enter your username:")
print("Greetings!", Username, "Welcome back to our shop:)")

budget= int(input("Now, Enter your budget:"))
print("Your Budget is:", budget)

save= int(input("Please Enter your minimum saving amount, So you can buy wihtin your budget:"))
print("So, You want to save", save, "at the end of shopping.")

print(Username,", what would you like to buy?")

choice= int(input("Press '1' for Apple(300/kg).\nPress '2' for Pineapple(90/piece).\nPress '3' for Mango(350/kg).\nPress '4' for Grapes(120/kg).\nPress '5' for Orange(150/kg)."))
# choice= input("Press '1' for Apple(300/kg).\nPress '2' for Pineapple(90/piece).\nPress '3' for Mango(350/kg).\nPress '4' for Grapes(120/kg).\nPress '5' for Orange(150/kg).")
# choice= int("Please Enter your choice:")   

#This progame gives negative values too       
if choice == 1:
    if(budget-300>=save):
        print("Purchased 1kg Apples, You saved:", budget-300, "Thankyou ForShopping with us :).")
    else:
        print("Sorry! You need", abs(budget-300-save), "more to buy this fruit ,so you can have",  save, " in your pocket.")

if choice == 2:
    if(budget-90>=save):
        print("Purchased 1kg Pineapples, You saved:", budget-90, "Thankyou ForShopping with us :).")
    else:
        print("Sorry! You need", abs(budget-90-save), "more to buy this fruit ,so you can have",  save, " in your pocket.")

if choice == 3:
    if(budget-350>=save):
        print("Purchased 1kg Mango, You saved:", budget-350, "Thankyou ForShopping with us :).")
    else:
        print("Sorry! You need", abs(budget-350-save), "more to buy this fruit ,so you can have",  save, " in your pocket.")

if choice == 4: 
    if(budget-120>=save):
        print("Purchased 1kg Grapes, You saved:", budget-120, "Thankyou ForShopping with us :).")
    else:
        print("Sorry! You need", abs(budget-120-save), "more to buy this fruit ,so you can have",  save, " in your pocket.")

if choice == 5:    
    if(budget-150>=save):
        print("Purchased 1kg Orange, You saved:", budget-150, "Thankyou ForShopping with us :).")
    else:
        print("Sorry! You need", abs(budget-150-save), "more to buy this fruit ,so you can have",  save, " in your pocket.")

else:
    print("Hope we will see you again:)\n Terminating the program!")
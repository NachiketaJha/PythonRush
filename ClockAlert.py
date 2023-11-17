import time
User = input("Who are you?")
print("Oh my lord! The almighty", User, ", you're here!")
timestmp = time.strftime('%H:%M:%S')
print("The Current time is:", timestmp)
hour = int(input("Enter hour to verify code:"))
hour = int(time.strftime('%H'))
# print(timestmp)
# timestmp = int(time.strftime('%M'))
# print(timestmp)
# timestmp = int(time.strftime('%S'))
# # print(timestmp)
# https://docs.python.org/3/library/time.html#time.strftime
if(hour==0 and hour<2):
    print(User, "Lord! Your Midnight snacks are waiting for you:)")
elif(hour>=2 and hour<=4):
    print(User, "Lord! Pls get some sleep T_T ")
elif(hour>4 and hour<7):
    print(User, "Lord! Did you skipped your sleep again?")
elif(hour>=7 and hour<9):
    print("Goodmorning", User, "Lord! Don't Forget to drink 1lt of lukewarm water.")
elif(hour==9 and hour<12):
    print(User, "Lord! Let's do some work:)")
elif(hour==12 and hour<14):
    print(User, "Lord! It's Lunch Time!")
elif(hour==14 and hour<=17):
    print(User, "Lord! Afternoon Sleep can ruin your day:(")
elif(hour>17 and hour<=20):
    print(User, "Lord! I think you should get some refreshment:)")
elif(hour>20 and hour<=22):
    print(User, "Lord! Everyone is waiting on Dinner table:P")
elif(hour>=23):
    print(User, "Lord! I think you should get some sleep:)")
else:
    print("YAWN! I NEED SOME SLEEP(￣o￣) . z Z")
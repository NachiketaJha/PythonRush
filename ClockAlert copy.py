import time
User = input("Who are you?")
print("Oh my lord! The almighty", User, ", you're here!")
timestmp = time.strftime('%H:%M:%S')
print("The Current time is:", timestmp)
timestmp = int(time.strftime('%H'))
# print(timestmp)
# timestmp = int(time.strftime('%M'))
# print(timestmp)
# timestmp = int(time.strftime('%S'))
# # print(timestmp)
# https://docs.python.org/3/library/time.html#time.strftime
if(timestmp==0 and):
    print(User, "Lord! Your Midnight snacks are waiting for you:)")
elif(timestmp<=4, timestmp>0):
    print(User, "Lord! Pls get some sleep T_T ")
elif(timestmp>4, timestmp<7):
    print(User, "Lord! Did you skipped your sleep again?")
elif(timestmp>7, timestmp<12):
    print("Goodmorning", User, "Lord! Don't Forget to drink 1lt of lukewarm water.")
elif(timestmp==12, timestmp<=14):
    print(User, "Lord! It's Lunch Time!")
elif(timestmp>17, timestmp<20):
    print(User, "Lord! I think you should get some refreshment:)")
elif(timestmp<22, timestmp>20):
    print(User, "Lord! Everyone is waiting on Dinner table:P")
elif(timestmp>=23):
    print(User, "Lord! I think you should get some sleep:)")
else:
    print("YAWN! I NEED SOME SLEEP(￣o￣) . z Z")
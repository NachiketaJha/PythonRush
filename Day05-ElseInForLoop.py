for i in range(6):
    print(i)
    if i == 4:
        break
else:                   #This will not execute as it will execute only when loop exits normally
    print("Oh no!")
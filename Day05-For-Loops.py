#for Loop
#range(A, B, step)- step basically skips in the section
print("All odd no. between 1 to 30")
for o in range(0, 30, 2):
    print(o+1, end=",")
    if o+1 ==13:
        print("--Many believe This too be a cursed no.")

print("All even no. between 1 to 30")
for e in range(1, 30, 2):
    print(e+1, end=",")
    if e+1 ==4:
        print("--Japanese believe This too be a cursed no.")
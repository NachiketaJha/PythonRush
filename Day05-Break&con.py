i = int(input("Which Number's Multiplication Table you want?"))
n = int(input("Specify count (till 20):"))

for n in range(0, 20):
    if(n==21):
        print("Task Performed!")
        continue
    print(i*n)
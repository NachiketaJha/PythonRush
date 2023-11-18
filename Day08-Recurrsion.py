#Recurrsion concept
#Calling a fn within itself
def fac(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fac(n-1))

num = int(input("Enter a no. to find factorial:"))
print(fac(num))

#fibonacci number
# f(0) = 0
# f(1) = 0
# f(2) = f(1) + f(0)
# f(x) = f(x-1) + f(x-2)

def f(x):
    if(x==0):
        return 0
    elif(x==1):
        return 1
    else:
        return(f(x-1)+f(x-2))

x = int(input("Find Fibonacci of term:"))
print(f(x))
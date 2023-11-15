#Average of Numbers
def avg(*num): # '* ' iterates so we can use multiple
    sum=0
    for i in num:
        sum = sum + i
    return sum/len(num)

a = avg(5,7,1)
print(a)
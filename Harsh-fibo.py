user_input = int(input("Enter"))
x = 1
y = 2

z = y 
i = 1
while i <= user_input:
    print(z, end=" ")
    i += 1
    x, y = y, z
    z = x+ y
       
print()
    

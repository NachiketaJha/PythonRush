#list - ordered collection/ indexed items/ mutable
L = [3, 4, 5, "Nachiketa", True]
print(L)
print(type(L))
print(L[3])
print(L[-3]) #length-3
print(L[1:4])
print(L[1:4:2])

lst=[i for i in range(4)] #list comprehension
print(lst)
lst=[i*i for i in range(10)]
print(lst)
lst=[i*2 for i in range(10) if i%2==0]
print(lst)
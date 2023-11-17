#tuples are immutable
tup = (1, "Nachiketa", 90, 999, "HEY")
# print(type(tup), tup)
# print(tup[-1])

# tup2 = tup[:3]
# print(tup2)

#Tuple Operations
a = tup.count(90)
b = tup.index(999)
c = tup.index(999, 1, 4)
# print(a, b, c)
d = len(tup)
print(c, d)

#Conversion of tuple to list so we can edit tuple

l = list(tup)
l.append("INDIA")
l.pop(4)
tup = tuple(l)
print(tup)
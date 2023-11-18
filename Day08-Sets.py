#Sets doesnt include repeated values and no order
# EmptySet = set()
# print(type(EmptySet))

S1 = {1, 2, 3, 4, "Hey!", 1, 22}
# for a in S1:
#     print(a)
S2 = {"A", 11, 22}
# S1 = S1.update(S2)
S3 = S1.union(S2)
S4 = S1.intersection(S2)
# S5 = S1.union(S2) - S1.intersection(S2)
S5 = S1.symmetric_difference(S2)
# print(S1.union(S2))
# print(S1, S2)
print(S3)
print(S4)
print(S5)
print(S1.isdisjoint(S2)) #Nothing in common = True else False
print(S1.issuperset(S2)) #Find Father/Whether elements of S2 in S1
print(S1.issubset(S2)) #Find Son/ Whether elements of S1 in S2

S1.add("Added!")
Pop1 = S1.pop() #Random
print(S1)
print(Pop1)

S2.clear()
print(S2)
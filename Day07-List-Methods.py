l = [69, 420, 1, 2, 8]
print(l)
l.append(1)
l.sort(reverse=True)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))

m = l.copy()
m[0] = 0
l.insert(1,29)
print(l)

m= [29, 39, 49]
l.extend(m)
k =l+m
print(l)
print(k)
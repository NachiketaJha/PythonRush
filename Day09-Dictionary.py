# print("Hey I'm back")
#key value points

emp = {1: 'Nachiketa', 2: 'Akash', 3:'Ganesh'}

print(emp.items())
for key, value in emp.items():
    print(f"The corressponding Employee id {key} is {value}")

#Methods
ep1 = {4: 'Harsh', 5:'Om'}
emp.update(ep1)
print(emp)
ep1.popitem(5)
ep1.clear()
del ep1[4]
print(ep1)

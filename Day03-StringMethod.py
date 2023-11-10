#Strings are immutable (in place) but you can edit a new coppy
a = "nachIketA"
print(a)
print(len(a))
print(a.upper())
print(a.lower())

b = "!!!Nachiketa!! !Nach!!!"
print(b.rstrip("!")) #Excludes string from right/end not from begining
print(b.replace("Nach", "Crack"))
print(b.split(" "))

print(a.capitalize()) #CAPITALIZE first word, rest small

print(a.center(25))
print(len(a.center(25)))

print(b.count("ch"))
print(b.endswith("ch")) #checks and answer in boolean
print(b.endswith("!!")) #checks and answer in boolean
print(b.endswith("ch")) #checks and answer in boolean
print(b.endswith("ch", 2,7)) #checks between ranges

d = "He's chad and he is above our understanding"
print(d.find("is")) # -1 for absence, if present returns index
print(d.find("ishh")) # -1 for absence, if present returns index
print(d.index("is")) #similar but if we sure it is present then it shows error
print(d.isalnum()) #Checks if characters consist of A-Z, a-z or 0-9
print(a.isalnum()) #Checks if characters consist of A-Z, a-z or 0-9
print(a.islower())
print(a.isprintable()) # False - if detects characters like /n for next line

c = "    "  
print(c.isspace()) # True - Only when white spaces (Tab/Spacebar)

print(a.istitle())
print(a.isupper())
print(a.swapcase())

print(a.title()) #converts into title

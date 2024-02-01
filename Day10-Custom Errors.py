# a =int(input("Enter a value between 10-20 otherwise quit to exit"))

# if(a>20 or a<10):
#     raise ValueError("Value should be between 10 and 20")

# # elif(a =! "quit"):
# #     raise SyntaxError("Pls write quit correctly")
   
# else:
#     print(f"Your {a} is valid")

a =input("Enter a quit")
if(a != "quit"):
    raise SyntaxError("Pls write quit correctly")
else:
    print("Thanks for choosing us :-)")
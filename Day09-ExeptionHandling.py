# n = input("Enter the num:")
# print(f"Multiplication of {n} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(n)}x{i} = {int(n)*i}")
# except ValueError:
#     print("Invalid Input!")
# except IndexError:
#     print("Invalid Index!")

def fun():
    try:
        l = [1,3,5,7,9]
        i = int(input("Enter the address:"))
        print(l[i])
        return 1
    except ValueError:
        print("Invalid Input!")
        return 0
    except IndexError:
        print("Invalid Index!")
        return 0
    finally:                        #Sometimes Print might not work when errors are throwed.
        print("Orewa Dio!")

x = fun()
print(x)
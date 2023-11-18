#DocString - Fn with description
#Written right below fn or above body
# PEP8 - Python Enhancement Proposal/ Guidelines -"import this" to print Zen of python.
def square(n):
    '''Takes an input then provides a square'''
    print(n**2)
square(56)
print(square.__doc__)

# It`s calculator, it tackes x and y and operator from the user, and shows the result of the operation
x = float(input("Tap first number: "))
y = float(input("Tap second number: "))
opr = input("Tap operator: ")

def sum(x, y):
    print(f"The sum of the numbers is: {x+y:.2f}")

def difference(x, y):
    print(f"The difference of the numbers is: {x-y:.2f}")

def multiplication(x, y):
    print(f"The multiplication of the numbers is: {x*y:.2f}")

def degree(x, y):
    print(f"The degree of the numbers is: {x/y:.2f}")

if opr == "+": 
    sum(x, y)  
elif opr == "-":
    difference(x, y)
elif opr == "*":
    multiplication(x, y)
elif opr == "/":
    degree(x, y)
else:
    print("Symbol entered incorrectly")





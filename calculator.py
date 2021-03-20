# first_name = input("What`s your name? ").capitalize()
# last_name = input("What`s your surname? ").capitalize()

# def hello(n, s):
#     print(f"Hello, {n} {s}!")

# def name(n):
#     print(f"Your name is: {n}")

# def surname(s):
#     print(f"Your surname is: {s}")

# def initial(n, s):
#     print(f"Your initials are: {n:.1}. {s:.1}.")

# hello(first_name, last_name)
# name(first_name)
# surname(last_name)
# initial(first_name, last_name)
# 4 функции(деф) - название функции(сумма/умножение)
# если ввести оператор +, тогда запускается функция (условие на проверку и внутри вызов функции)
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
    print("Знак введен неверно")





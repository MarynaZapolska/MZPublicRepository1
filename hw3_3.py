import math
a = float(input("Ведіть перше число: "))
op = input("Виберіть операцію: +, -, *, /, зведення в ступінь (g2), квадратний корінь(sqrt), cos, tg ")

result = " "

if op != "**" and op != "sqrt" and  op != "cos" and  op != "tg":
    b = float(input("Ведіть друге число: "))

if op == "+": result = a + b
elif op == "-": result = a - b
elif op == "*": result = a * b
elif op == "/": result = a / b

elif op == "sqrt": result = math.sqrt(a)
elif op == "cos": result = math.cos(a)
elif op == "tg": result = math.tan(a)
elif op == "g2": result = a**b

print("Результат = ", result)
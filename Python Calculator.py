def add(a, b):
    return a + b
def substract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Simple Python Calculator")
print("Choose an operation: a, s, m, d")

op = input("Operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if op == "a":
    print("Result:", add(num1, num2))
elif op == "s":
    print("Result:", substract(num1, num2))
elif op == "m":
    print("Result:", multiply(num1, num2))
elif op == "d":
    print ("Result:", divide(num1, num2))
else:
    print ("Invalid operation")

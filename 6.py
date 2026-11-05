a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")
d = input("Enter Boolean (True/False): ").lower() == "true"

# Display values and data types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
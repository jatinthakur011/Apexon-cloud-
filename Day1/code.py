# Simple calculator
a = 10
b = 5
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

# output->Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0

# Even or ODD
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output->ODD

# Swap numbers
a = 5
b = 10
a, b = b, a
print(a, b)

#output-> a=10 b=5

# Sum of first n natural number
n = 5
total = 0
for i in range(1, n+1):
    total += i
print(total)
# output->15
s = "Python"
print(s[1:4])      # Output: yth
print(s[:])        # Output: Python
print(s[2:])       # Output: thon
print(s[:3])       # Output: Pyt
print(s[0:6:3])    # Output: Ph
print(s[::-1])     # Output: nohtyP

s = "python programming"

print(s.upper())        # Output: PYTHON PROGRAMMING
print(s.lower())        # Output: python programming
print(s.capitalize())   # Output: Python programming
print(s.title())        # Output: Python Programming
print(s.swapcase())     # Output: PYTHON PROGRAMMING

print(len(s))           # Output: 18
print(s.count("p"))     # Output: 2
print(s.find("pro"))    # Output: 7
print(s.index("pro"))   # Output: 7

print(s.startswith("python"))  # Output: True
print(s.endswith("ing"))       # Output: True
s = "Hello"


a = "Hello bhai kese ho"
print(len(a))
# Output: 18
print(a.title())
# Output: Hello Bhai Kese Ho
print(a.strip())
# Output: Hello bhai kese ho
print(a.replace("H", "h"))
# Output: hello bhai kese ho
print(a.split())
# Output: ['Hello', 'bhai', 'kese', 'ho']
print("-".join(a))
# Output: H-e-l-l-o- -b-h-a-i- -k-e-s-e- -h-o
print("hello\nworlds")
# Output:
# hello
# worlds

# iterations over string
for ch in a:
    print(ch)

# Mutable vs Immutable
x = 10
print(id(x))   # Output: (memory address example)
x = x + 5
print(id(x))   # Output: different memory address

a = [10, 20, 30]

a[0] = 100
print(id(a))
# Output: same memory address

# freq. of characters
s = "hello"
for i in s:
    print(i, ":", s.count(i))
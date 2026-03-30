# Find second  number
nums = [10, 25, 15]
largest = nums[0]
second = nums[0]

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second Largest:", second)
# output--> 15

# Type checking
x = 10
print(type(x))
# output --> <class 'int'>


# decimal module
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)
# output-> 0.3

# operator precedence
result = 10 + 5 * 2
print(result)
# output-> 20
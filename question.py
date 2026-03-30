#  Input Example:
# [("IT", 5000), ("HR", 3000), ("IT", 4000)]

# Expected Output Example:
# {"IT": 9000, "HR": 3000}

data=[("IT",5000),("HR",3000),("Tech",4000)]
result={}
for dept, salary in data:
    result[dept]=result.get(dept,0)+salary
print(result)

max_dept = None
max_salary = 0

for dept in result:
    if result[dept] > max_salary:
        max_salary = result[dept]
        max_dept = dept

print(max_dept, max_salary)



# Input: "abbbccd" 
# Output: "a1b3c2d1"

s = "abbbccd"
result = ""
count = 1
for i in range(len(s)):
    # check next character
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
print(result)


# Input: ["apple", "bat", "ball", "cat"]
# Output: {
#   "a": ["apple"],
#   "b": ["bat", "ball"],
#   "c": ["cat"]
# }

words = ["apple", "bat", "ball", "cat"]
result = {}
for word in words:
    first_char = word[0]   
    if first_char not in result:
        result[first_char] = []
    result[first_char].append(word)
print(result)
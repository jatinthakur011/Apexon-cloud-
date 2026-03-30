student={
    "name":["hi","hello"],
    "age":20,
    "course":"CSE"
}
#loop through keys
for key in student:
    print(key)

#loop through values
for value in student.values():
    print(value)

for key,value in student.items():
    print(key,": ",value)

#check key exists
if "name" in student:
    print("key exist")

# length of dictonary
print(len(student))

for ch in student.get("name"):
    print(ch)
student={
    "name":"jatin",
    "age":20,
    "course":"CSE"
}
#access dictonary values
print(student["name"])#if wrong input than error
# or
print(student.get("name"))#if wrong input than print none

#update and add new
student["age"]=21
student["city"]="bilaspur"
print(student)

# remove specific item
student.pop("age")
print(student)

#remove last item
student.popitem()
print(student)

#delete using del
del student["course"]
print(student.get("course"))

#clear dictonary
student.clear()
print(student)

# dictonary methods
# keys()
print(student.keys())# print all keys not values

#values()
print(student.values())#print only values

#items()--> output-> key +value pairs
print(student.items())

#update()
student.update({"age":22,"course":"cse"})
print(student.items())

#copy()
new_student=student.copy()
print(new_student)

#setdefault()  -> add only if key is not present
student.setdefault("country","India")
print(student)


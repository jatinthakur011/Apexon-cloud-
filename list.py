marks=[90.0,45.0,66.4,90.1]
print(marks)
print(len(marks))
print(marks[1:3])

#list methods

list=[6,3,4,2,1]
list.append(10)
list.sort(reverse=True)
list.reverse()
list.insert(1,7)
print(list)

list=[2,1,3,1]
list.pop(2)
list.remove(1)
print(list)

a=[]
a.append(input("enter ist movies: "))
a.append(input("enter 2nd movies: "))
a.append(input("enter 3rd movies: "))
b=a.copy()
b.reverse()
if a==b:
    print("palindrome")
else:
    print("not palindrome")


#even or odd
a=int(input("enter the number: "))
if a%2==0:
        print("even number")
else:
    print("Odd number")

#maximum value in list

a=list(map(int,input("Enter the number: ").split()))
max_val=a[0]
for i in a:
    if i>max_val:
        max_val=i
print("max value: ",max_val)        

#check prime number in list
num=int(input("Enter the number: "))
if num<=1:
    print("not prime number")
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("not prime")
        else:
            print("prime")

a=list(map(int,input("Enter the number: ").split()))
sum=0
for i in a:
    sum+=i
print(sum)    


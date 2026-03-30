s="Python"
print(s[1:4])#yth
print(s[:]) #Python
print(s[2:])#thon
print(s[:3])#pyt
print(s[0:6:3])
print(s[::-1])

#immutable
s="Hello"
s[0]="J"#Type error doesnot support
s="J"+s[1:]
print(s)

#string functions
a="Hello bhai kese ho"
print(len(a))
print(a.title())#make every words first char capital
print(a.strip())#remove leading spaces
print(a.replace("H","h"))
print(a.split())
print("-".join(a))
print("hello\nworlds")

#iteration 
for ch in a:
    print(ch)

#mutable & immutable
x=10
print(id(x))
x=x+5
print(id(x))

a=[10,20,30]
# print(id(a))
a[0]=100
print(id(a))

#frequency of character
s=input("enter the string: ")
for i in s:
    print(i,":",s.count(i))

s=input("Enter the string: ")
checked=""
for ch in s:
    if ch not in checked:
        count=0
        for c in s:
            if ch==c:
                count+=1
        print(ch,":",count)
        checked+=ch

s=input("enter the string: ")
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)


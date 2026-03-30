# count vowels---->
s="educAtIon"
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1
print(count)

# Another approach

list=['a','e','i','o','u']
s="jatin thakur"
count=0
for ch in s:
    if ch in list:
        count+=1
print(count)

# frequency of each character----->

s="jatin @%&! t&*hakur"
freq={}
for ch in s:
    if ch.isalpha():
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
print(freq)

# using if cond...

s="jatin @%&! t&*hakur"
freq={}
for ch in s:
    if (ch>='a' and ch<='z' or ch>='A' and ch<='Z'):
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
print(freq)


# Reverse a string ---->

s="student"
rev=""
for ch in s:
    rev=ch+rev
print(rev)

# using slicing
s="student"
print(s[::-1])

# using inbuilt reverse 
rev=""
s="student"
s=rev.join(reversed(s))
print(s)

# check palindrome ----->

s=input("enter a string: ")
if s==s[::-1]:
    print("is Palindrome")
else:
    print("not palindrome")

s=input("enter the string: ")
rev=""
for char in s:
    rev=char+rev
if(rev==s):
    print("Palindrome")
else:
    print("Not palindrome")

# remove spcaes ----->
s=" hello  wo r ld"
rev=""
for char in s:
    if char !=' ':
        rev+=char
print(rev)

# alternative
s=" hello worl d "
print(s.replace(' ',''))

# count words ---->

s=input("enter the string: ")
count=1
if s=='':
    print(0)
else:
    for ch in s:
        if ch==' ':
            count+=1
    print(count)

s=input("enter the string: ")
print(len(s.split()))

#reverse the string without changing order

s = "my name is jatin"
rev = ""
word=""
for char in s:
    if char != " ":
        rev = char + rev 
    else:
        word+=rev+" " 
        rev=""
word+=rev
print(word)

s = "my name is jatin"
words=s.split() 
result=""
for w in words:
    result+=w[::-1]+" "
print(result.strip())

# I/P: I am a student.
# O/P: I ma a tneduts.

s="I am a student."
result=""
word=""
for ch in s:
    if ch.isalpha():
        word=ch+word
    else:
        result+=word+ch
        word=""
print(result)

# reverse alternative
s="my name is jatin"
result=""
word=s.split()
for i in range(len(word)):
    if i%2==1:
        result=result+word[i][::-1]+' '
    else:
        result=result+word[i]+' '
print(result.strip())


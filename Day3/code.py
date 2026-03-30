# dictonary methods
s="programming @#12jatin"
freq={}
for ch in s:
    if ch.isalpha():
        freq[ch]=freq.get(ch,0)+1
print(freq)
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 2, 'm': 2, 'i': 2, 'n': 2, 'j': 1, 't': 1}

# find first repeating character
s=input("enter the string: ")
freq={}
result=""
for ch in s:
    if ch in freq:
        result=ch
        break
    else:
        freq[ch]=freq.get(ch,0)+1
print(result)
# Output: r

# non repeating character
s=input("enter the string: ")
freq={}
result=""
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for ch in s:
    if freq[ch]==1:
        print(ch)
        break
# Output: p

# find duplicate characters

s="programming"
freq={}
list=[]
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
for char in freq:
    if freq[char]>1:
        list.append(char)
print(list)
# Output: ['r', 'g', 'm']

# another approach using set
s="programming"
seen=set()
duplicate=set()
for char in s:
    if char in seen:
        duplicate.add(char)
    else:
        seen.add(char)
print(duplicate)
# Output: {'r', 'g', 'm'}

# check anagram ------>
s=input("enter first string: ")
m=input("enter second string: ")
if sorted(s) ==sorted(m):
    print("anagram")
else:
    print("not anagram")
# Output: anagram

# another approach using dictonary
s=input("enter first string: ")
m=input("enter second string: ")
freq={}
for char in s:
    freq[char]=freq.get(char,0)+1
for char in m:
    if char not in freq or freq[char]==0:
        print("not anagram")
        break
    freq[char]-=1
else:
    print("Anagram")
# Output: Anagram

# most frequent character
s="heeeeellloooo"
freq={}
for char in s:
    freq[char]=freq.get(char,0)+1
maxfreq=0
maxchar=""
for char,value in freq.items():
    if value > maxfreq:
        maxfreq=value
        maxchar=char
print(maxchar)
# Output: e

# remove duplicate
s="aabccbdeefgh"
seen=set()
result=""
for char in s:
    if char not in seen:
        result+=char
        seen.add(char)
print(result)
# Output: abcdefgh

# check all alphabets exist or not
s= "the quick #$ br%&*own fox jumps over a lazy dog in the"
letters=set()
for char in s:
    if char.isalpha():
        letters.add(char.lower())
print(len(letters)==26)
# Output: True
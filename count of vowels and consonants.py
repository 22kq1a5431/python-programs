n=input("Enter a string: ")
vowels="aeiouAEIOU"
v=0
c=0
for ch in n:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
print("vowels:", v)
print("consonants:",c)

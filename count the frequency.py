n=input("Enter a string: ")
f ={}
for c in n:
    if c in f:
        f[c] += 1
    else:
        f[c] = 1
print(f)

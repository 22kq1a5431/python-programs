n=input()
def palin(p):
    p=p.lower().replace(" ","")
    return p==p[::-1]
print(palin(n))

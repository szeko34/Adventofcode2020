subor=open("6_1input.txt","r")

s=subor.read().split("\n\n")

abc="qwertzuioplkjhgfdsayxcvbnm"

suc=0

for r in s:
    a=r.split("\n")
    print(a)
    for i in abc:
        if all([i in j for j in a]):
           suc+=1

print(suc)

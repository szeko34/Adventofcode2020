subor=open("6_1input.txt","r")# Tu napíšte svoj kód :-)

s=subor.read().split("\n\n")

abc="qwertzuioplkjhgfdsayxcvbnm"
print(len(abc))

suc=0

for r in s:
    a=r.split("\n")
    print(a)
    for i in abc:
        #print(i,[i in j for j in a])
        if all([i in j for j in a]):
            #print(i,[i in j for j in a])
            suc+=1

print(suc)

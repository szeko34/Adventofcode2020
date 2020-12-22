subor = open("22_1input.txt", "r")

hraci=subor.read().split("\n\n")

deky=[x.split("\n") for x in hraci]
A=[int(x) for x in deky[0][1:]]
B=[int(x) for x in deky[1][1:]]


print(A,B)

while A and B:
    a=A.pop(0)
    b=B.pop(0)
    if a>b:
        A=A+[a,b]
    else:
        B=B+[b,a]
    print(A,B)

if A:
    vys=A
else:
    vys=B

print(vys)

suc=0
for i in range(len(vys)):
    suc+=(len(vys)-i)*vys[i]

print(suc)

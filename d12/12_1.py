subor=open("12_1input.txt","r")

r=subor.readlines()

inst=[]

for x in r:
    x=x.strip()
    inst.append((x[0],int(x[1:])))

otocenia=[(1,0),(0,1),(-1,0),(0,-1)]
smer=0
print(inst)
vzd=[0,0]
for s,d in inst:
    print(s,d, vzd)
    if s == "F":
        vzd[0] += otocenia[smer][0] * d
        vzd[1] += otocenia[smer][1] * d
    if s == "N":
        vzd[1] += -d
    if s == "S":
        vzd[1] += d
    if s == "E":
        vzd[0] +=  d
    if s == "W":
        vzd[0] += -d
    if s == "R":
        smer = (smer + (d // 90)) % 4
    if s == "L":
        smer = (smer - (d//90)) % 4

print (vzd, abs(vzd[0])+abs(vzd[1]))





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
wp=[10,-1]
for s,d in inst:
    print(s,d, vzd, wp)
    if s == "F":
        vzd[0] += wp[0] * d
        vzd[1] += wp[1] * d
    if s == "N":
        wp[1] += -d
    if s == "S":
        wp[1] += d
    if s == "E":
        wp[0] +=  d
    if s == "W":
        wp[0] += -d
    if s == "R":
        for i in range (d // 90):
            wp[0],wp[1] = -wp[1],wp[0]
    if s == "L":
        for i in range (d // 90):
            wp[1],wp[0] = -wp[0],wp[1]

print (vzd, abs(vzd[0])+abs(vzd[1]))





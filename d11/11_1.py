subor=open("11_1input.txt","r")

pole = []

riadky=[x.strip() for x in subor.readlines()]

pole.append(list("."*(len(riadky[0])+2)))

for x in riadky:
    pole.append(list("."+x+"."))

pole.append(list("."*(len(riadky[0])+2)))

#print(pole)

def susedov(p,x,y):
    tmp = 0
    for i in -1,0,1:
        for j in -1,0,1:
            tmp += p[x+i][y+j] == "#"
    if p[x][y] == "#":
        return tmp - 1
    else:
        return tmp

def vypis(pole):
    for x in pole:
        print(x)

def krok(p):
    nove=[list("."*(len(riadky[0])+2))]
    for i in range(1,len(p)-1):
        r=["."]
        for j in range(1,len(p[0])-1):
            #print(susedov(p,i,j))
            if p[i][j] == "L" and susedov(p,i,j) == 0:
                r.append("#")
            elif p[i][j] == "#" and susedov(p,i,j) >= 4:
                r.append("L")
            else:
                r.append(p[i][j])
        r.append(".")
        nove.append(r)
    nove.append(list("."*(len(riadky[0])+2)))
    #vypis(nove)
    return(nove)

nove=pole
stare = []
k=0
while nove != stare:
    stare=nove
    nove=krok(stare)
    k += 1
    print(k)

sedadiel = 0
for x in nove:
    sedadiel+= x.count("#")

print(sedadiel)


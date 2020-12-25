smer={"e":(2,0),"ne":(1,-1),"nw":(-1,-1),"se":(1,1),"w":(-2,0),"sw":(-1,1)}
print(smer)

subor=open("24_1input.txt","r")

r=subor.readlines()
tiles={}

for riadok in r:
    cesta=[]
    z=""
    for i in range(len(riadok)):
        z+=riadok[i]
        if riadok[i] in "we":
            cesta.append(z)
            z=""
    print(riadok,cesta)
    x,y=0,0
    for k in cesta:
        #print(smer[k])
        x+=smer[k][0]
        y+=smer[k][1]
        #print(x,y)
    if (x,y) in tiles.keys():
        tiles[(x,y)]=not tiles[(x,y)]
    else:
        tiles[(x,y)]=True

def susedov(p,x,y):
    tmp = 0
    for k in smer:
        if (x+smer[k][0],y+smer[k][1]) in p.keys():
            tmp += p[(x+smer[k][0],y+smer[k][1])]==True
    return tmp

def den(p):
    novyden={}
    for k in p:
        if p[k]:
            if 0==susedov(p,k[0],k[1]) or susedov(p,k[0],k[1])>2:
                novyden[k]=False
            else:
                novyden[k]=True
        else:
            if susedov(p,k[0],k[1])==2:
                novyden[k]=True
            else:
                novyden[k]=False
        for a in smer:   #pridanie okolitych
            if not (k[0]+smer[a][0],k[1]+smer[a][1]) in novyden:
                novyden[(k[0]+smer[a][0],k[1]+smer[a][1])]=False
    return novyden


novy={}
for b in tiles.keys():
    novy[b]=tiles[b]
    for a in smer:
        if not (b[0]+smer[a][0],b[1]+smer[a][1]) in tiles:
            novy[(b[0]+smer[a][0],b[1]+smer[a][1])]=False
tiles=novy
print(tiles)
print(len([x for x in tiles if tiles[x]==True]))

for i in range(100):
    tiles=den(tiles)
   # print(i,len([x for x in tiles if tiles[x]==True]))
print(i,len([x for x in tiles if tiles[x]==True]))

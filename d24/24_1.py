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
        x+=(smer[k][0])
        y+=smer[k][1]
        #print(x,y)
    if (x,y) in tiles.keys():
        tiles[(x,y)]=not tiles[(x,y)]
    else:
        tiles[(x,y)]=True



print(len([x for x in tiles if tiles[x]==True]))

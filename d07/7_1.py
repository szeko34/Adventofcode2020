subor=open("7_1input.txt","r")

s=subor.readlines()

kody=[]
prav={}

for r in s:
    r=r.split()
    prav[r[0]+r[1]]=[]
    for i in range(5,len(r),4):
        prav[r[0]+r[1]].append(r[i]+r[i+1])


vsetky=[]
nieco=True
prve=["shinygold"]
kolko=0
while nieco:
    druhe=[]
    nieco=False
    for x in prav:
        for f in prve:
            if f in prav[x] and all(not x in b for b in vsetky) and not x in druhe:
                nieco=True
                druhe.append(x)

    vsetky.append(druhe)
    kolko+=len(druhe)
    print(vsetky)
    prve=[a for a in druhe]

print("\n\n",vsetky,len(vsetky),kolko)

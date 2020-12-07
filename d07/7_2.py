subor=open("7_1input.txt","r")

s=subor.readlines()

kody=[]
prav={}

for r in s:
    r=r.split()
    prav[r[0]+r[1]]=[]
    for i in range(5,len(r),4):
        if not r[i]+r[i+1]=="otherbags.":
            print(r[i]+r[i+1])
            prav[r[0]+r[1]].append((r[i]+r[i+1],r[i-1]))

vsetky=[]
nieco=True
prve=[["shinygold",1]]
kolko=0

def vyhodnot(ktore):
    for p in ktore:
        if prav[p[0]]==[]:
            return int(p[1])
        else:
            return int(p[1])+int(p[1])*sum([vyhodnot(list([x])) for x in prav[p[0]]])

print(vyhodnot(prve)-1)


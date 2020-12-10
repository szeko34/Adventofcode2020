subor=open("10_1input.txt","r")

import sys
sys.setrecursionlimit(500000)


cisla=[int(x) for x in subor.readlines()]
cisla.sort()

print (cisla)

"""
#prva cast
j=1 if cisla[0]==1 else 0
t=2 if cisla[0]==3 else 1

for i in range(len(cisla)-1):
    j+= cisla[i+1]-cisla[i]==1
    t+= cisla[i+1]-cisla[i]==3

print(j,t,j*t)
"""
cisla=[0]+cisla
cisla.append(max(cisla)+3)
prud=max(cisla)
i=0
moznosti=[]

mnoziny=[]
i=0
tmp=[]
while i<len(cisla)-1:
    if cisla[i+1]-cisla[i]<3:
        tmp.append(cisla[i])
    else:
        tmp.append(cisla[i])
        mnoziny.append(tmp)
        tmp=[]
    i+=1
print(mnoziny)

def spocitaj(z,prud):
    #print(prud,end=" ")
    if prud==min(z):
        #print("M")
        return 1
    elif prud in z:

        tmp = spocitaj(z,prud-1)+spocitaj(z,prud-2)+spocitaj(z,prud-3)
        #print("moznosti pre prud",prud)
        return (tmp)
    else: return 0

vysledok=1
for m in mnoziny:
    print(spocitaj(m,max(m)))
    vysledok*=spocitaj(m,max(m))

print(vysledok)

#print(spocitaj(cisla,max(cisla)))

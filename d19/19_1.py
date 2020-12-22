subor = open("19_1i.txt", "r")

r = subor.read().split("\n\n")

pravidla=r[0].split("\n")

print(pravidla)
nove=[]
for x in pravidla:
    x=x.split()
    nx=""
    for a in x:
        if a.isdigit():
            nx+=a.zfill(3)+" "
        else:
            nx+=a+" "
    nove.append(nx)

print(nove)

pravidla=nove

priklady=r[1].split("\n")

graf={}

m=0
for p in pravidla:

    p=p.replace("\"","")

    k,p=p.split(":")
    p=p[1:].split(" | ")
    p=[x.split() for x in p]
    k=k.zfill(3)
    print(p)
    if p==[["a"]]:
        p="a"
        kdea=k
    elif p==[["b"]]:
        p="b"
        kdeb=k

    graf[k]=p

print(graf)

pouzite=[x for x in graf.keys()]
pouzite.sort(reverse=True)

print(pouzite)

re42=repr("042")

rex=repr(graf["000"])
def vyraz(rex):
    menim=True
    while menim:
        menim = False
        for c in pouzite:
            #print(c)
            if c in rex:
                #print("aha",c)
                #pouzite.pop(pouzite.index(c))
                #print(pouzite)
                menim = True
                rex=rex.replace(c,repr(graf[c]))
        #print(rex)


    rex=rex.replace(" ","")
    rex=rex.replace("],[",")|(")
    rex=rex.replace(",","")
    rex=rex.replace("\'","")
    rex=rex.replace("[","(")
    rex=rex.replace("]",")")
    return rex

rex=vyraz(repr(graf["042"]))
print(rex)
print(vyraz(repr(graf["031"])))



import re

prog=re.compile(rex)

sedi=0
for a in priklady:
    print(a, end=" ")
    sedi+= not re.fullmatch(rex,a)==None
    print(re.fullmatch(rex,a))

print(sedi)

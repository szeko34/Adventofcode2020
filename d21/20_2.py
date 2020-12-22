subor = open("21_1input.txt", "r")

suroviny=set()
alergeny={}
vyskyt={}

for x in subor:
    print(x[:-1])
    sur=x.split(" (contains")[0]


    al=x[:-2].split(" (contains")[1]

    al=al.strip().split(", ")
    sur=sur.split()
    for s in sur:
        suroviny.add(s)
        if not s in vyskyt.keys():
            vyskyt[s]=0
        vyskyt[s]+=1

    print(sur,al)
    for a in al:
        if not a in alergeny.keys():
            alergeny[a]=[]
        alergeny[a].append(set(sur))

print(alergeny,suroviny,vyskyt)

for a in alergeny:
    print(a)
    result=alergeny[a][0]
    for i in range(1,len(alergeny[a])):
        print(i)
        result=result.intersection(alergeny[a][i])
    alergeny[a]=result
    print(a,result)
    for s in result:
        if s in suroviny:
            suroviny.remove(s)
    print(suroviny)

print(alergeny,suroviny,vyskyt)

suc=0
for s in suroviny:
    suc+=vyskyt[s]

print(suc)
al=[x for x in alergeny.keys()]
al.sort()
print(al)
slovo={}
hladam=True
while hladam:
    hladam=False
    for a in alergeny:
        print(a)
        if len(alergeny[a])==1:
            sl=next(iter(alergeny[a]))
            print("AA",sl)
            slovo[a]= sl
            for a in alergeny:
                if sl in alergeny[a]:
                    alergeny[a].remove(sl)
            hladam=True
            break

print(slovo)
result=""
for a in al:
    result+=slovo[a]+","

print(result[:-1])




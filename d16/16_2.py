subor = open("16_1input.txt", "r")

cely = subor.read().split("\n\n")

pravidla = cely[0].split("\n")

prav = {}

c = set()

cisla = {}
kategorie = []

for x in pravidla:
    p = x.split(":")[0]
    kategorie.append(p)
    x = x.split()
    a, b = x[-1].split("-")
    for i in range(int(a), int(b) + 1):
        c.add(i)
        if i in cisla:
            cisla[i].append(p)
        else:
            cisla[i] = [p]
    a, b = x[-3].split("-")
    for i in range(int(a), int(b) + 1):
        c.add(i)
        if i in cisla:
            cisla[i].append(p)
        else:
            cisla[i] = [p]
    prav[p] = c
    c = set()

#vytvorim mnozinu pripustnych cisel, bude to zjednotenim vsetkych cisel z jednotlivych pravidiel
c = set()
for x in prav:
    c = c.union(prav[x])


r = cely[2].split("\n")

# vyrobenie zoznamu platnych listkov
novy = []
for i, x in enumerate(r[1:]):
    nechaj = True
    for a in x.split(","):
        if not int(a) in c:
            nechaj = False
            break
    if nechaj:
        novy.append(x.split(","))
# z dat jednotlivych platnych listkov vyrobim stlpce
stlpce = []
for i in range(len(novy[0])):
    stlpce.append([x[i] for x in novy])
# idem vytvorit zaznam, kde ku kategorii priradim stlpe, v ktorom je aplikovana
vys = {}
while kategorie:
    for i in range(len(stlpce)):
        kolko = 0
        kde = (
            []
        )  # tu si budem pamatat, v ktorych stlpcoch je mozne tuto kategoriu mat, ak bude jedina, tak ju vyhodim zo zoznamu kategorii a do vysledku o tom pridam zaznam
        for k in kategorie:
            kde.append(
                all([k in cisla[int(a)] for a in stlpce[i]])
            )  # nachadza sa kategoria vo vsetkych cislach daneho stlpca?
            kolko += all([k in cisla[int(a)] for a in stlpce[i]])
        if kolko == 1:  # je taky stlpec len jediny?
            vys[kategorie.pop(kde.index(True))] = i
            break
# toto je moj listok
c = [int(x) for x in cely[1].split("\n")[-1].split(",")]

su = 1  # ziskanie finalneho sucinu
for x in vys:
    if "departure" in x:
        a = c[vys[x]]
        su = su * a
print(su)

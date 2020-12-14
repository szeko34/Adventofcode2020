subor = open("14_1input.txt", "r")

r = subor.readlines()

h = {}

def mask(maska, cislo):
    result = ""
    cislo = list("{0:036b}".format(int(cislo)))
    for i in range(len(maska)):
        if maska[i] == "X":
            result += maska[i]
        elif maska[i] == "1":
            result += "1"
        else:
            result += cislo[i]
    return list(result)

def adresy(maska):
    global z
    if not "X" in maska:
        z.append(maska)
        return z
    else:
        m1 = [x for x in maska]
        m2 = [x for x in maska]
        m1[maska.index("X")] = 1
        m2[maska.index("X")] = 0
        adresy(m1)
        adresy(m2)

for x in r:
    if x[:4] == "mask":
        maska = list(x[-37:-1])
    else:
        z = []
        adresy(mask(maska, (x[x.find("[") + 1 : x.find("]")])))
        for i in z:
            adr = int("".join([str(a) for a in i]), 2)
            h[adr] = int(x.split()[-1])

print(sum(h.values()))

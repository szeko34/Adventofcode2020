subor = open("14_1input.txt", "r")

r = subor.readlines()

h = {}

def spoj(maska, cislo):
    tmp = "{0:036b}".format(cislo)
    result = ""
    for i in range(len(maska)):
        if maska[i] != "X":
            result += maska[i]
        else:
            result += tmp[i]
    return result

for x in r:
    if x[:4] == "mask":
        maska = x[-37:-1]
    else:
        h[x[x.find("[") + 1 : x.find("]")]] = int(spoj(maska, int(x.split()[-1])), 2)

print(sum(h.values()))

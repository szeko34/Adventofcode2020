cisla = [int(x) for x in "0,5,4,1,10,14,7".split(",")]

i = 7

c = {}
for j in range(len(cisla)):
    c[cisla[j]] = j
dalsi = 0

while i < (30000000 - 1):
    if dalsi not in c.keys():
        c[dalsi], dalsi = i, 0
    else:
        c[dalsi], dalsi = i, i - c[dalsi]
    i += 1
print(dalsi)

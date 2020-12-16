subor = open("16_1input.txt", "r")

cely = subor.read().split("\n\n")

pravidla = cely[0].split("\n")

c = set()

for x in pravidla:
    x = x.split()
    a, b = x[-1].split("-")
    for i in range(int(a), int(b) + 1):
        c.add(i)
    a, b = x[-3].split("-")
    for i in range(int(a), int(b) + 1):
        c.add(i)

r = cely[2].split("\n")

neplatne = 0

for x in r[1:]:
    for a in x.split(","):
        if not int(a) in c:
            neplatne += int(a)

print(neplatne)

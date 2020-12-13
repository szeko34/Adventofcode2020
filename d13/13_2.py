subor = open("13_1input.txt", "r")

n = int(subor.readline())

z = subor.readline().split(",")

cisla = []
for i in range(len(z)):
    if z[i] != "x":
        cisla.append([int(z[i]), i])

cisla.sort(reverse=True)

i = 0
x = cisla[i][0] - cisla[i][1]
inc = cisla[i][0]


while i < len(cisla) - 1:
    while ((x + cisla[i + 1][1]) % cisla[i + 1][0]) != 0:
        x += inc
    inc *= cisla[i + 1][0]
    i += 1
print(x)

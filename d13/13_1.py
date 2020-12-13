subor = open("13_1input.txt", "r")

n = int(subor.readline())

cisla = [int(x) for x in subor.readline().split(",") if x != "x"]

najmensi = n
vys = 0

for x in cisla:
    if x - n % x < najmensi:
        najmensi, vys = x - n % x, x * (x - n % x)

print(vys)

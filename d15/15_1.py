cisla = [int(x) for x in "0,5,4,1,10,14,7".split(",")]

i = 6


while i < (2020 - 1):
    if cisla.count(cisla[i]) == 1:
        cisla.append(0)
    else:
        cisla.append(i - (len(cisla) - cisla[-2::-1].index(cisla[i]) - 2))
    i += 1

print(len(cisla), cisla[-1])

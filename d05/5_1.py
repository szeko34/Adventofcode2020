# Tu napíšte svoj kód :-)
subor=open("5_1input.txt","r")# Tu napíšte svoj kód :-)

s=subor.readlines()

z=[int(x[:7].replace("B","1").replace("F","0"),2)*8+int(x[-4:-1].replace("L","0").replace("R","1"),2) for x in s]
z.sort()

for i in range(z[0],z[-1]):
    if not i in z:
        print(i)
        break

print(max(z))

# Tu napíšte svoj kód :-)

subor=open("3_1input.txt","r")

r=subor.readlines()
n=len(r)
pole=[list(x.strip()) for x in r]

x=0
y=0
stromA=0
while y<n:
    if pole[y][x]=="#":
        stromA+=1
        print("TU",end=" ")
    print(x,y)
    x=(x+1)%len(pole[y])
    y+=1

x=0
y=0
stromB=0
while y<n:
    if pole[y][x]=="#":
        stromB+=1
        print("TU",end=" ")
    print(x,y)
    x=(x+3)%len(pole[y])
    y+=1

x=0
y=0
stromC=0
while y<n:
    if pole[y][x]=="#":
        stromC+=1
        print("TU",end=" ")
    print(x,y)
    x=(x+5)%len(pole[y])
    y+=1

x=0
y=0
stromD=0
while y<n:
    if pole[y][x]=="#":
        stromD+=1
        print("TU",end=" ")
    print(x,y)
    x=(x+7)%len(pole[y])
    y+=1

x=0
y=0
stromE=0
while y<n:
    if pole[y][x]=="#":
        stromE+=1
        print("TU",end=" ")
    print(x,y)
    x=(x+1)%len(pole[y])
    y+=2


print(stromA,stromB,stromC,stromD,stromE,stromA*stromB*stromC*stromD*stromE)

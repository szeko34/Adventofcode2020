poradie=[int(x) for x in "198753462"]
print(poradie)
n=len(poradie)
co=1

for i in range(100):
    cast=poradie[1:4]
    print(cast)
    poradie=[poradie[0]]+poradie[4:]
    poradie=poradie+poradie
    print(poradie)
    kam=poradie[0]-1
    if kam==0:
        kam=n
    while kam not in poradie:
        kam=kam-1
        if kam==0:
            kam=n
    poradie=poradie[:poradie.index(kam)+1]+cast+poradie[poradie.index(kam)+1:]
    print("vlozene",poradie)
    poradie=poradie[1:n+1]
    print(poradie)

result=poradie+poradie
res=""
for i in range(result.index(1)+1,result.index(1)+n):
    res=res+str(result[i])

print(res)

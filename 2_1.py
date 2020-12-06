# Tu napíšte svoj kód :-)

subor=open("2_1input.txt","r")

r=subor.readlines()
kolko=0
for x in r:
    a=int(x.split()[0].split("-")[0])
    b=int(x.split()[0].split("-")[1])
    p=x.split()[1][0]
    text=x.split()[-1]
    if (text[a-1]==p or text[b-1]==p) and text[b-1]!=text[a-1]:
        kolko+=1
print(kolko)

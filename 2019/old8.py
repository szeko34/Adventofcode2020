# Tu napíšte svoj kód :-)
subor=open("19input.txt","r")

mi="0"*25*6
message=["2"]*25*6

while True:
    lay = subor.read(25*6)
    for i in range(len(lay)):
        if message[i]=="2":
            message[i]=lay[i]
    if lay == '':
        break
    if lay.count("0")<mi.count("0"):
        mi=lay

print(mi.count("1")*mi.count("2"))
for i in range(6):
    print("".join(message[i*25:i*25+25]).replace("0"," ").replace("1","X"))

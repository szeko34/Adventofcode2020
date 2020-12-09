subor=open("8_1inputa.txt","r")

riadky=subor.readlines()
z=[]
for x in riadky:
    z.append(x.split())

i=0
suc=0
while z[i]!="":
    print(i,z[i])
    if z[i][0]=="nop":
        z[i]=""
        i+=1
    elif z[i][0]=="acc":
        suc+=int(z[i][1])
        z[i]=""
        i+=1
    elif z[i][0]=="jmp":
        pom=int(z[i][1])
        z[i]=""
        i+=pom



print (suc)


#print(z)


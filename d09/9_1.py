subor=open("9_1input.txt","r")

cisla=[int(x) for x in subor.readlines()]


def vyhodnot(a,i,d):
    for x in cisla[i-d:i]:
        if (a-x) in cisla[i-d:i] and x!=(a-x):
            return True
    return False

#od zaciatku sa pre kazdych 25 overuje vyhodnotenie
i=25
d=25
while vyhodnot(cisla[i],i,d):
    i+=1

#cyklus skonci na
print(cisla[i])


#cast2
n=cisla[i]
i=0
j=i
suc=0

#ked presiahnem dany sucet, tak sa posuniem o prvok dalej
while suc!= n:
    if suc>n:
        suc=0
        i+=1
        j=i
    else:
        suc+=cisla[j]
        j+=1

print(min(cisla[i:j])+max(cisla[i:j]))

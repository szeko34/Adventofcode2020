subor = open("18_1input.txt", "r")

r = [x.strip() for x in subor.readlines()]


n=6
roz=(n+1)*2+len(r[0])

pole=[[[["." for a in range(roz)] for a in range(roz)]for a in range(roz)] for a in range((n+1)*2+1)]

#vypisanie pola
def vypis(x):
    for a in x:
        for b in a:
            for c in b:
                for d in c:
                    print(d,end=" ")
            print()
        print()



#dopisanie hodnot zo zadania
for i in range(len(r)):
    for j in range(len(r[i])):
        pole[n+1][n+1][n+1+i][n+1+j]=r[i][j]

"""
vypis(pole)
print("--------------")
"""

def susedia(p,x,y,z,w):
    s=0
    for a in (-1,0,1):
        for b in (-1,0,1):
            for c in (-1,0,1):
                 for d in (-1,0,1):
                    s+= p[x+a][y+b][z+c][w+d]=="#"
    if p[x][y][z][w]=="#":
        return s-1
    else:
        return s

def krok(p,i):
    np=[[[["." for a in range(roz)] for a in range(roz)]for a in range(roz)]for a in range(roz)]
    for a in range(n-i+1,(n+1)*2 -(n-i)):
        for b in range(n-i+1,roz-(n-i)-1):
            for c in range(n-i+1,roz-(n-i)-1):
                for d in range(n-i+1,roz-(n-i)-1):
                    #print(a,b,c,p[a][b][c],susedia(p,a,b,c) )
                    if p[a][b][c][d]=="." and susedia(p,a,b,c,d)==3:
                        np[a][b][c][d]="#"
                        #print("aha")
                        #vypis(np)
                    elif p[a][b][c][d]=="#" and susedia(p,a,b,c,d) in (2,3):
                        np[a][b][c][d]="#"
                    else:
                        np[a][b][c][d]="."
    #print("np")
    #vypis(np)
    return(np)

for i in range(n):
    pole=krok(pole,i+1)
    #print(i)
    #vypis(pole)

def zrataj(x):
    suc=0
    for a in x:
        for b in a:
            for c in b:
                for d in c:
                    suc += d=="#"
    return suc

print(zrataj(pole))

subor = open("22_1input.txt", "r")

hraci=subor.read().split("\n\n")

deky=[x.split("\n") for x in hraci]
A=[int(x) for x in deky[0][1:]]
B=[int(x) for x in deky[1][1:]]


#print(A,B)
def game(A,B):
    stavy=[]
    while A and B:
        #print(A,B)
        #print("stavy",stavy)
        if A in stavy:
            print("tu")
            return 1
        stavy.append([x for x in A])
        a=A.pop(0)
        b=B.pop(0)
        if round(a,b,A,B)==1:
            A=A+[a,b]
        else:
            B=B+[b,a]
        #print("po kole",a,b,A,B)
    if A:
        print(A)
        suc=0
        for i in range(len(A)):
            suc+=(len(A)-i)*A[i]

        print(suc)
        return 1
    else:
        print(B)
        suc=0
        for i in range(len(B)):
            suc+=(len(B)-i)*B[i]

        print(suc)
        return 2

def round(a,b,A,B):
    #print("round",a,b,A,B,len(A),len(B))
    if a>len(A) or b>len(B):
        if a>b:
            return 1
        else:
            return 2
    else:
        #print("rek")
        return game(A[:a],B[:b])


vys=game(A,B)
print(A,B,vys)


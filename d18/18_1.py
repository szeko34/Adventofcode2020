subor = open("18_1inputt.txt", "r")

r = [x.strip() for x in subor.readlines()]

def rozdel(x):
    l=""
    p=""
    c=0
    #print("delim: ",x,len(x))
    if len(x)<=1:
        return [x]
    while c<len(x):
        if x[c] in "+*":
            l+=x[c]
            #print(l,(x[c+1:]))
            return [rozdel(l[:-1]),[x[c]],rozdel(x[c+1:])]
        elif x[c]=="(":
            zatvorky=["("]
            c+=1
            while zatvorky:
                if x[c]==")":
                    zatvorky.pop()
                if x[c] == "(":
                    zatvorky.append("(")
                l+=x[c]
                #print(l,zatvorky)
                c+=1
            #print("dvojica: ",l,(x[c+1:]))
            if len(x[c+1:])>=1:
                return [rozdel(l[:-1]),[x[c]],rozdel(x[c+1:])]
            else: return([rozdel(l[:-1])])
        else:
            if x[c] != ")":
                l+=x[c]
            c+=1



def vyhodnot(x):
    if len(x)==1 and not type(x) is list and x.isdigit():
        return int(x)
    elif len(x)==1:
        return (vyhodnot(x[0]))
    elif x[1]==["+"]:
        return vyhodnot(x[0])+vyhodnot(x[2])
    else :
        return vyhodnot(x[0])*vyhodnot(x[2])

suc = 0
for x in r:
    x=x.replace(" ","")
    #print(repr(x))
    print(vyhodnot((rozdel(x))))

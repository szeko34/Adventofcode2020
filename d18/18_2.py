subor = open("18_1input.txt", "r")

r = [x.strip() for x in subor.readlines()]

def vyhodnot(x):
    if not type(x) is list:
        #print("aha",x,type(x))
        return (x)
    else:
        for i in range(0,len(x)-2,2):
            if x[i+1]=="+":
                x[i+2]=vyhodnot(x[i])+vyhodnot(x[i+2])
            elif x[i+1]=="*":
                x[i+2]=vyhodnot(x[i])*vyhodnot(x[i+2])
        return((vyhodnot(x[-1])))

suc=0
for x in r:
    x=x.replace(" * ","],\"*\",[")
    x=x.replace(" ",",")
    x=x.replace("+","\"+\"")
    x=x.replace(" ",",")
    x=x.replace("(","[[")
    x=x.replace(")","]]")
    x="[["+x+"]]"
    x=eval(x)
    print(x)
    suc+=int(vyhodnot(x))

print(suc)

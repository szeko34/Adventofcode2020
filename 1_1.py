subor=open("1_1input.txt","r")

cisla=[int(x) for x in subor]
for x in cisla:
    r=(2020-x)
    for y in cisla:
        if (r-y) in cisla:
            print(x*y*(r-y),x,y,r-y)
            break

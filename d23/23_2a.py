poradie=[int(x) for x in "198753462"]

from collections import deque
import numpy as np

print(poradie)
n=len(poradie)
kolko=1000000
for i in range(n+1,kolko+1):
    poradie.append(i)
co=1

items=np.array(poradie)

for i in range(10000000):
    #print(items)

    """
    if i%1000==0:
        print(i)
    """
    #items=np.roll(items,-1)
    cast=items[1:4]
    dalsi=items[0]
    items=np.append(items[4:],dalsi)

    #print("odsekni",cast,items)

    #items=np.concatenate(([items[0]],items[4:]))


    kam=items[-1]-1
    #print(kam)
    if kam==0:
        kam=kolko
    while kam in cast:
        kam=kam-1
        if kam==0:
            kam=kolko
        #print(kam)
    items=np.roll(items,kolko-3-((np.where(items==kam)[0])+1))
    #print("nastav",kam,items)
    items=np.append(items,cast)
    #print("posun",items)
    items=np.roll(items,-1-(np.where(items==dalsi)[0]))
    #print("spat",dalsi,items)

for i in range(int(np.where(items==1)[0]+1),int(np.where(items==1)[0]+1+2)):
    print(items[i])

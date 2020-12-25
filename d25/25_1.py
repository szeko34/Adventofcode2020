
cp=15628416
dp=11161639
"""

cp=5764801
dp=17807724
"""
i=1
res=1

while res!=cp and res!=dp:
    res=(res*7)%20201227
    i+=1

print(i-1,res)

res=1
for j in range(i-1):
    res=(res*dp)%20201227

print(res)





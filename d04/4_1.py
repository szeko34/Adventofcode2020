# Tu napíšte svoj kód :-)

hladam=("byr","iyr","eyr","hgt","hcl","ecl","pid")

subor=open("4_1input.txt","r")
z=[x.replace("\n"," ").split() for x in subor.read().split("\n\n")]

kolko=0
ok=0
for x in z:
    je=0
    d="".join(x)
    for a in hladam:
        je+= d.count(a)==1
    kolko+= je == 7
    if je==7:
        x=dict([a.split(":") for a in x])
        print(kolko,(x))
        if (
            1920<=int(x["byr"])<=2002
            and 2010<=int(x["iyr"])<=2020
            and 2020<=int(x["eyr"])<=2030
            and x["hgt"][:-2].isdigit()
            and ((x["hgt"][-2:]=="cm" and 150<=int(x["hgt"][:-2])<=193) or (x["hgt"][-2:]=="in" and 59<=int(x["hgt"][:-2])<=76))
            and x["hcl"][0]=="#" and len(x["hcl"])==7 and len([a for a in x["hcl"][1:] if a.isdigit() or "a"<=a<="f"])==6
            and x["ecl"] in ("amb","blu","brn","gry","grn","hzl","oth")
            and x["pid"].isnumeric() and len (x["pid"])==9
            ):
                ok+=1
                print(kolko)

print(kolko,ok)

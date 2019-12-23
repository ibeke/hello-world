import math

#mérési eredmények - tömb
adat1=[]   #idő
adat2=[]   #pl. x pozició
#feldolgozandó mérési eredmények száma
darab=0
#számolt adatok  - tömb
szamolt1=[]
szamolt2=[]

#beolvasás

darab=int(input("Mérési adatokpárok száma="))

for i in range(0,darab,1):
    adat1.append(float(input("1-tömb eleme=")))
    adat2.append(float(input("2-tömb eleme=")))
    print("\")

print("Adat1 elemei:",adat1)
print("Adat2 elemei:",adat2)

#feldolgozás
# -első differenciák
i=0
for i in range(0,darab,1):
    if i==darab-1:
        break
    else:
        delta1=(adat2[i+1]-adat2[i])/(adat1[i+1]-adat1[i])
        szamolt1.append(delta1)

print("\n")
# -második differenciák    
i=0
for i in range(0,darab,1):
    if i==darab-2:
        break
    else:
        delta2=(szamolt1[i+1]- szamolt1[i])/(adat1[i+1]-adat1[i])
        szamolt2.append(delta2)

#eredmény megjelenítés
if darab<2:
    print("Nem számolhatók a második differenciák")
else:
    print("Első differenciák ")
    print(szamolt1)
    print("Második differenciák ")
    print(szamolt2)

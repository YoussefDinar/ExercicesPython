
# moyenne d'une collection de valeurs entrées#
L = []
i=0
val=1
while val!=0:
    if val!=0:
        val=float(input(f"Type a value {i+1} "))
        L.append(val)
        i=i+1
    else:
        break

somme=0
for k in L:
    somme+=k

Moy=somme/(i-1)
print(f"La moyenne : {Moy}")



         #BINAIRE EN DECIMAL#
def binaryToDec(n):
    return int(n,2)
print (binaryToDec('1100'))



 #TYPE DU TRIANGLE#

L1= float(input("Entrer la longueur 1 du triangle \n"))
L2= float(input("Entrer la longueur 2 du triangle \n"))
L3= float(input("Entrer la longueur 3 du triangle \n"))

if L1==L2 and L2==L3:
    print("Le triangle est equilatéral \n")
elif L1==L2 and L3!=L2 or L2==L3 and L1!=L2 or L1==L3 and L2!=L1:
    print("Le triangle est isocèle \n")
else:
    print("Le triangle est scalène \n")  



# DECIMAL EN BINAIRE #
def DecToBin(number):
        if number >= 1:
            DecToBin(number // 2)
            print (number % 2) 

DecToBin(12)
def sumatorio (numero):
    suma=0
    for i in range (numero,0,-1):
        suma=suma+i
    return suma

num=int(input("introduzca un entero"))
print (sumatorio(num))

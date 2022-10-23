def factorial (numero):
    multiplicacion=0
    for i in range (numero,0,-1):
        multiplicacion=multiplicacion*i
    return multiplicacion

num=int(input("introduzca un entero"))
print (factorial(num))

def iva (precio):
    precio_iva=precio*1.21
    return precio_iva

coste=float(input("introduzca precio sin iva ...") )
print (iva(coste))
    

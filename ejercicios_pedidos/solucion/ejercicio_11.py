def factorial (numero):
    facto=1
    for i in range (numero,0,-1):
        facto=facto*i
    return facto

num=int(input("introduzca un número entero ...") )
print (factorial(num))
    

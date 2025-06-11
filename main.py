#Ejercicio 1
def suma(num1,num2):
    return num1+num2

#Ejercicio 2
def saludo(nombre):
    print(f"Saludos {nombre}")

#Ejercicio 3
def par_impar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))    
print(suma(num1,num2))
nombre = input("Ingrese su nombre: ")
print(saludo(nombre))
numero = int(input("Ingrese un numero: "))
par_impar(numero)
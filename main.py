num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
def suma(num1,num2):
    return num1+num2
nombre = input("Ingrese su nombre: ")
def saludo(nombre):
    print(f"Saludos {nombre}")
numero = int(input("Ingrese un numero: "))
def par_impar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")        
print(suma(num1,num2))
print(saludo(nombre))
par_impar(numero)
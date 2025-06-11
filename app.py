lista = []
salir = False
numeros = []

def validar_lista_numeros():
    try numeros.append(int(input("Ingrese numeros separados por espacios: "))):
    except (ValueError):
        print("Ingrese un valor entero")
while salir == False:
    validar_lista_numeros()
    for i in numeros:
        print(i)
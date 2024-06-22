# Tareas de Python 
import math

def es_pangrama(cadena):
    import string
    cadena = cadena.lower()  # Convertir a minúscula
    alfabeto = string.ascii_lowercase + "ñ"  # Hablamos español, si no, quítale la ñ
    for letra in alfabeto:  #Recorrer el alfabeto
        if letra not in cadena:  # Si una letra del alfabeto no está, sabemos que no es pangrama
            return False
    # Si recorrimos todas las letras, terminamos el ciclo
    # y por lo tanto todas estuvieron, así que:
    return True


def areaTriangulo(base, altura):
    return (base * altura)/2


def generar_primos_en_rango(inicio, fin):
    primos = []

    termino = 1    
    for numero in range(inicio, fin + 1):                
        if es_primo(numero):            
            primos.append(numero)             
    return primos


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True


def SumarNumeros(lista, numero):
    for x in range(1, numero+1):      
        lista.append(x)    

    suma = sum(lista)
    print(lista)
    return suma


def ContarOcurrencias(lista, numero):
    for x in range(numero):      
        lista.append(numero)    

    return lista


def PromedioLista(lista):
    Promedio = sum(lista) / len(lista)    
    return Promedio

def OrdenaLista(lista):
    lista.sort()
    print(lista)

print("")
print("1. Ordenar una lista")
print("Escribe una función que reciba una lista de números y devuelva una nueva lista con los elementos ordenados de manera ascendente.")

mi_lista = [67, 2, 999, 1, 15]
OrdenaLista(mi_lista)

# mi_lista.sort()
# print("Lista Ordenada : ", mi_lista)

print("")
print("2. Calcular el promedio de una lista")
print("Escribe una función que reciba una lista de números y devuelva el promedio de esos números.")


mi_lista = [67, 2, 999, 1, 15]
print("Lista",mi_lista)
print("Promedio...",PromedioLista(mi_lista))

print("")
print("3. Contar ocurrencias de un elemento")
print("Escribe una función que reciba una lista y un elemento, y devuelva el número de veces que ese elemento aparece en la lista.")
print("Ocurrencias ..",ContarOcurrencias([], 5))

print("")
print("4. Suma de los primeros n números naturales")
print("Escribe una función que reciba un número entero positivo 'n' y devuelva la suma de los primeros 'n' números naturales.")
print(SumarNumeros([], 10))
print("")
print("5. Eliminar duplicados de una lista")
print("Escribe una función que reciba una lista y devuelva una nueva lista sin elementos duplicados")
mi_lista = [2, 4, 4, 4, 4, 4, 9, 9]
mi_lista_sin_duplicados = list(set(mi_lista))
print(mi_lista)
print(mi_lista_sin_duplicados)
print("")
print("6. Generar números primos")
print("Escribe una función que genere los primeros 'n' números primos.")
primos_entre_1_y_50 = generar_primos_en_rango(1, 50)
print("Números primos entre 1 y 50:", primos_entre_1_y_50)
print("")
print("7. Calcular el área de un triángulo")
print("Escribe una función que reciba la base y la altura de un triángulo y devuelva su área")
print("Base: 7")
print("Altura: 4")
print("Area del Triangulo : ", areaTriangulo(7, 4))
print("")
print("8. Contar letras en una cadena")
print("Escribe una función que reciba una cadena y devuelva un diccionario con el conteo de cada letra en la cadena.")

cadena = "hola como estas, que es de tu vida"

letras = set(cadena)            ##La filtracion de los duplicados genera una tupla

letras = sorted(letras)         ##Se ordena la tupla 

sumasletras = {}

for x in letras:        
    cantidad = cadena.count(x)  
    sumasletras.update({x:cantidad})

print("------------------------")
print("cadena string : ",cadena)
print("diccionario de la suma de cada letra : ", sumasletras)
print("")

print("9. Verificar si una cadena es un pangrama")
print("Escribe una función que reciba una cadena y devuelva True si es un pangrama (contiene todas las letras del alfabeto al menos una vez) y False en caso contrario.")
print("")
cadenas_para_probar = [
    "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado en una caja de zinc que pesó un kilo",  # No
    "Hola",  # No
    "aeiou",  # No
    "parzibyte",  # No
    "abcdefghijklmnñopqrstuvwxyz",  # Sí
    "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja",  # Sí,
    "abcdefghijklmnopqrstuvwxyz",  #No, porque no lleva ñ
    "Mi hijo degustó en el festival de bayas una extraña pizza de kiwi con queso",  #Sí
    "Hola como estan, que ha sido de tu vida",  #No
    "La cigueña tocaba el saxofón detrás del palenque de paja", #No
    "Fabio me exige, sin tapujos, que añada cerveza al whisky", #si
    "El veloz murciélago hindú comía feliz cardillo y kiwi", #no
]
print("")
for cadena in cadenas_para_probar:
    print("¿'{}', es un pangrama? {}".format(cadena, es_pangrama(cadena)))


print("")

print("10. Calcular el factorial de un número")
print("Escribe una función que calcule el factorial de un número entero no negativo.")
print("")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)

numero = 8
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")





# my_diccionario = {'a': 1, 'b': 2}
# nuevos_datos = {'c': 3, 'd': 4}
# my_diccionario.update(nuevos_datos)
# print(my_diccionario)

# print(letrax)

# print( letras{x} )
# cantidad = cadena.count(x)
# print(cantidad)
# sumasletras.append(cantidad)
# print(cadena[x])

# lista = [1, 3, 3, 4, 4, 5]
# cantidad_de_tres = lista.count(3)
# print(f"El número 3 aparece {cantidad_de_tres} veces en la lista.")




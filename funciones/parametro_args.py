#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,9,10,20,3])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])


#lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Lucas",5,3,9,10,20,3)

#------------------------------------------------------
def sumar(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Output: 15
# En este ejemplo, la función sumar utiliza *args como parámetro para aceptar un número variable de argumentos. Los argumentos se pasan como una secuencia de números separados por comas. La función recorre todos los argumentos y los suma, devolviendo el resultado.

# Ejemplo 2: Concatenación de cadenas


def concatenar(*args):
    resultado = ""
    for cadena in args:
        resultado += cadena
    return resultado

resultado = concatenar(f"Hola", " " ,"mundo","!")
print(resultado)  # Output: "Hola mundo!"
# En este ejemplo, la función concatenar acepta un número variable de argumentos de tipo cadena. Utiliza *args para recibir las cadenas y las concatena en orden para formar una única cadena de salida.

# Ejemplo 3: Pasar una lista como argumentos individuales

def multiplicar(a, b, c):
    return a * b * c

numeros = [2, 3, 4]
resultado = multiplicar(*numeros)
print(resultado)  # Output: 24
# En este ejemplo, la lista numeros se pasa como argumento utilizando *numeros. Esto desempaqueta la lista y pasa sus elementos como argumentos individuales a la función multiplicar, que realiza la multiplicación de los números y devuelve el resultado.

# En resumen, el operador *args permite a una función recibir un número variable de argumentos. Puede utilizarse para sumar números, concatenar cadenas o desempaquetar una lista en argumentos individuales, entre otros usos.
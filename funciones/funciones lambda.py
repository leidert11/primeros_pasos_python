numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#creando funcion comun que diga si es par o no
#def es_par(num):
#    if (num%2==1):
#        return True
    
#usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))

#-----------------------------------------------------------

# Ejemplo 1: Ordenar una lista de números de menor a mayor:

numeros = [4, 2, 7, 1, 5]
numeros.sort(key=lambda x: x)
print(numeros)  # Output: [1, 2, 4, 5, 7]
# En este ejemplo, la función lambda lambda x: x devuelve el mismo valor x. Al pasar esta función lambda como la clave de ordenación al método sort(),
# la lista numeros se ordena de menor a mayor.

# Ejemplo 2: Ordenar una lista de cadenas por su longitud:

palabras = ['manzana', 'pera', 'banana', 'kiwi']
palabras.sort(key=lambda x: len(x))
print(palabras)  # Output: ['kiwi', 'pera', 'banana', 'manzana']
# En este caso, la función lambda lambda x: len(x) devuelve la longitud de cada cadena x. Al utilizar esta función lambda como clave de ordenación,
# la lista palabras se ordena de acuerdo a la longitud de las cadenas, de menor a mayor longitud.

# Ejemplo 3: Filtrar elementos de una lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4, 6, 8, 10]
# En este ejemplo, la función lambda lambda x: x % 2 == 0 se utiliza como función de filtrado. Solo se incluirán en la lista pares
# aquellos números x para los cuales la expresión x % 2 == 0 es verdadera, es decir, los números pares.

# Espero que estos ejemplos te ayuden a comprender mejor la función lambda y su uso en diferentes contextos.
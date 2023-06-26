# Ejemplos de datos compuestos en Python

# Lista (list)
mi_lista = [1, 2, 3, 4, 5]
# Especificación:
# - La lista es una colección ordenada de elementos.
# - Permite duplicados y mantiene el orden de inserción.
# - Los elementos se pueden acceder mediante índices (0-based index).
# - Los elementos de la lista son mutables, es decir, se pueden modificar.
# - Ejemplo de acceso: mi_lista[2] devuelve el valor 3.
# - Ejemplo de modificación: mi_lista[1] = 10 cambia el valor en la posición 1 a 10.

# Tupla (tuple)
mi_tupla = (1, 2, 3, 4, 5)
# Especificación:
# - La tupla es una colección ordenada de elementos.
# - Permite duplicados y mantiene el orden de inserción.
# - Los elementos se pueden acceder mediante índices (0-based index).
# - Los elementos de la tupla son inmutables, es decir, no se pueden modificar.
# - Ejemplo de acceso: mi_tupla[2] devuelve el valor 3.
# - No se pueden modificar los elementos de una tupla.

# Conjunto (set)
mi_conjunto = {1, 2, 3, 4, 5}
# Especificación:
# - El conjunto es una colección desordenada de elementos únicos.
# - No permite duplicados y no mantiene un orden específico.
# - Los elementos no se pueden acceder mediante índices ya que no tienen un orden definido.
# - Los elementos de un conjunto son mutables, es decir, se pueden agregar o eliminar.
# - Ejemplo de agregar elemento: mi_conjunto.add(6) agrega el valor 6 al conjunto.
# - Ejemplo de eliminar elemento: mi_conjunto.remove(2) elimina el valor 2 del conjunto.

# Diccionario (dict)
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
    }
# Especificación:
# - El diccionario es una colección de pares clave-valor.
# - Las claves son únicas y se utilizan para acceder a los valores correspondientes.
# - No hay un orden específico en los pares clave-valor.
# - Los elementos se pueden acceder mediante las claves.
# - Los elementos del diccionario son mutables, es decir, se pueden modificar.
# - Ejemplo de acceso: mi_diccionario["edad"] devuelve el valor 30.
# - Ejemplo de modificación: mi_diccionario["ciudad"] = "Barcelona" cambia el valor de "ciudad" a "Barcelona".

# Errores comunes:
# - IndexError: Se produce cuando se intenta acceder a un índice fuera del rango válido.
# - TypeError: Se produce cuando se intenta realizar una operación no válida en el tipo de dato.
# - KeyError: Se produce cuando se intenta acceder a una clave que no existe en un diccionario.

# Mostrar índices y valores:
# - En una lista, tupla o conjunto, se puede iterar utilizando un bucle for y obtener tanto el índice como el valor.
#   Ejemplo: for i, valor in enumerate(mi_lista):
#              print(f"Índice: {i}, Valor: {valor}")
# - En un diccionario, se pueden obtener las claves y los valores mediante los métodos keys() y values().
#   Ejemplo: for clave, valor in mi_diccionario.items():
#              print(f"Clave: {clave}, Valor: {valor}")

# Ejemplos de operaciones no permitidas:
# - No se puede modificar el valor de una tupla (ejemplo: mi_tupla[0] = 10).
# - No se puede acceder a los elementos de un conjunto mediante índices (ejemplo: mi_conjunto[0]).
# - No se puede acceder a una clave inexistente en un diccionario sin verificar su existencia previamente.
#   (ejemplo: mi_diccionario["apellido"])



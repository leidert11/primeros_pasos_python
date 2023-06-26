# Ejemplos de datos compuestos en Python

# Lista (list)
mi_lista = [1, 2, 3, 4, 5]
print("Lista:", mi_lista)

# Tupla (tuple)
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla:", mi_tupla)

# Conjunto (set)
mi_conjunto = {1, 2, 3, 4, 5}
print("Conjunto:", mi_conjunto)

# Diccionario (dict)
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
    }

print("Diccionario:", mi_diccionario)

# Errores comunes:
# - IndexError: Se produce cuando se intenta acceder a un índice fuera del rango válido.
print(mi_lista[10])  # Genera un IndexError

# - TypeError: Se produce cuando se intenta realizar una operación no válida en el tipo de dato.
print(mi_lista + mi_tupla)  # Genera un TypeError

# - KeyError: Se produce cuando se intenta acceder a una clave que no existe en un diccionario.
print(mi_diccionario["apellido"])  # Genera un KeyError

# Mostrar índices y valores:
for i, valor in enumerate(mi_lista):
    print(f"Índice: {i}, Valor: {valor}")

for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

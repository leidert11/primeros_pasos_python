# Input básico
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)

# Input numérico entero
edad = int(input("Ingrese su edad: "))
print("Usted tiene", edad, "años.")

# Input numérico de coma flotante
altura = float(input("Ingrese su altura en metros: "))
print("Su altura es", altura, "metros.")

# Input de múltiples valores
valores = input("Ingrese varios valores separados por espacio: ")
lista_valores = valores.split()  # Convierte los valores ingresados en una lista de cadenas
print("Valores ingresados:", lista_valores)

# Input de una lista de números
numeros = input("Ingrese una lista de números separados por coma: ")
lista_numeros = [float(x) for x in numeros.split(",")]  # Convierte los números ingresados en una lista de flotantes
print("Lista de números ingresados:", lista_numeros)

# Input de una sola tecla
tecla = input("Presione una tecla: ")
print("Tecla presionada:", tecla)

# Input con contraseña oculta
import getpass
contrasena = getpass.getpass("Ingrese su contraseña: ")
print("Contraseña ingresada:", contrasena)

# Input con selección de opción
opcion = input("Seleccione una opción (1, 2, 3): ")
if opcion == "1":
    print("Ha seleccionado la opción 1.")
elif opcion == "2":
    print("Ha seleccionado la opción 2.")
elif opcion == "3":
    print("Ha seleccionado la opción 3.")
else:
    print("Opción inválida.")

# Input con confirmación (sí o no)
confirmacion = input("¿Desea continuar? (sí/no): ")
if confirmacion.lower() == "sí":
    print("Continuando...")
else:
    print("Operación cancelada.")

# Input de fecha
from datetime import datetime
fecha_str = input("Ingrese una fecha (dd/mm/aaaa): ")
fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
print("Fecha ingresada:", fecha)

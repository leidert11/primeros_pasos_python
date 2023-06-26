#de esta manera se importa una funcion en especifica del archivo mencionado y se les cambia el nombre 
from funciones_buenas.saludar import saludar as primer_saludo,  saludar_diferente as segundo_saludo
# import funciones_buenas.saludar as m_saludar

saludo = primer_saludo("leider")

saludo_diferente = segundo_saludo("sindy")

#creamos las variables con los resultados 

print(saludo)
print(saludo_diferente)

#accedeos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamdo
# print(m_saludar.__name__)

#de esta manera se importa todo lo que alla en el archivo que hace 
# referencia y asignandole el nombre "m_saludar"

# import modulo_saludar2 as m_saludar

# saludo = m_saludar.saludar("leider")

#para ver las propiedades y metodos en el namespace
# print(dir(m_saludar))

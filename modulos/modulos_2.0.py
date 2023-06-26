#si el modulo estuviera dentro de una carpeta en las misma ruta
# import funciones_buenas.saludar as m_saludar

# print(m_saludar.saludar("tami"))

# print(m_saludar.saludar_diferente("leider"))

import sys

#ejemplo  las propiedades accedemosa asi : 
sys.path.append("d:\\Documentos\\python\\funciones_buenas")
# print(sys.path)

import saludar as modulo_saludo

print(modulo_saludo.saludar("python"))
print(modulo_saludo.saludar_diferente("ferney"))

#ejemplo : las funciones accedemos asi : 
# print(sys())

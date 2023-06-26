#matriz: conjunto de datos (list)
lista = ['leider','leider tami',False,1.85]
#tupla
tupla = ('leider','leider tami',False,1.82)

#la matriz si puede modificarse el tupla no 

#lista[2]=True success
#tupla[2]=True error


print(lista)
print(tupla)

#conjunto set : no tienen un orden fijo , son eementos desorddenados  y que peuden cambiar 

conjunto = {'leider','leider tami',False,1.81}

#se puede re definir pero no modificar los datos de los elementos 

#conjunto[0]= 'pepito' error
#conjunto= {'sindy','lorena torres',True,1.50} success

#ya que lo que imprime no viene en ordden tampoco se podra acceder al indice del set 
#print(conjunto[2]) error

#se puede acceder a un indice en especifico pero mediante un bucle
 
#en un conjunto no puede haber datos duplicados
#conjunto = {'leider','leider tami',False,1.81,'leider'} error

print(conjunto)

#creando un diccionrio (dict) (la estrutura es (key : value) y separamos por comas )

diccionario={
    'nombre':'leider',
    'apellido':'tami',
    'python':False,
    'altura':1.85
}

#para accedder a un elemento en especifico se muestra por el nombre asociado

print(diccionario['apellido'])
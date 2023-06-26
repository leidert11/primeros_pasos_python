#promeio de duraciones 

otros_cursos_min=2.5
otros_cursos_pro=4
otros_cursos_max=7
este_curso=1.5

#duracoin de video sin editar

duracion_otros_cursos=5
duracion_este_curso=3.5

#diferencis de duracion 

diferencia_cursos_min= 100- este_curso/otros_cursos_min*100
diferencia_cursos_max= 100- este_curso*1000//otros_cursos_max/10    
diferencia_cursos_pro= 100- este_curso/otros_cursos_pro*100

#calculando el porcentaje de duracion de video removido

timepo_vacio_promedio = 100- otros_cursos_pro*1000//duracion_otros_cursos/10  
timepo_vacio_este_curso = 100- este_curso*1000//duracion_este_curso/10  

#mostando las diferencias de duracion (ejercicio A)
print(f'este curso dura un {diferencia_cursos_min}% menos que el curso mas rapido')
print(f'este curso dura un {diferencia_cursos_max}% menos que el curso mas lento')
print(f'este curso dura un {diferencia_cursos_pro}% menos que el curso promedioo')

#mostraando la cantidad de espacio vacio que se remueve (ejercicio B)

print(f'un curso promedio elimina {timepo_vacio_promedio}% de tiempo vacio ')
print(f'un curso promedio elimina {timepo_vacio_este_curso}% de tiempo vacio ')

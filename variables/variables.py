#este tipo dde variable se puede modificar 
nombre = 'leider'
nombre = 'ferney'
nombre = 'tami'

print(nombre)

#conectar variables, en este caso numerico

numero= 10
numero +=2
numero -=2

print(numero)

#concatenar string 

name = 'ferney'
saludo = "hola " + name + ", ¿como estas?"
#esta forma toma cualquier dato y lo trasnforma en texto
saludo1 = f"hola {name} ¿como estas?"
# del borra la variable definida

print(saludo)
print(saludo1)

#operadores de pertenencia (in y not in)

# in busca algo que pidamos y retorna un boleano 
# not in busca allgo que no esta y retorna un boleano

print('hola' in saludo1) # true
print('hola' not in saludo1) # false
#creando una funciòn que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True


#creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        
    #devolvemos la lista
    return primos

#creamos el resultado llamando a la funciòn y lo mostramos
resultado = primos_hasta(98)
print(resultado)

#-------------------------------------------------

def obtener_numeros_primos(numero):
    primos = []
    for num in range(2, numero + 1):
        if es_primo(num):
            primos.append(num)
    return primos

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ejemplo de uso
limite = int(input("Ingrese un número límite: "))
numeros_primos = obtener_numeros_primos(limite)
print("resultado:", numeros_primos)


#-------------------------------------------------
def obtener_numeros_primos(numero):
    primos = []  # Lista para almacenar los números primos encontrados
    
    for num in range(2, numero + 1):  # Iterar desde 2 hasta el número dado (+1 para incluir el número)
        
        # Verificar si el número es primo utilizando un generador y la función all()
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primos.append(num)  # Agregar el número primo a la lista primos
    
    return primos  # Retornar la lista de números primos

resultado = obtener_numeros_primos(98)

print(f"resultado: {resultado} ")

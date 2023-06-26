#creando una funcion que muestre la serie fibonacci entre 0 el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(34)
print(resultado)

#----------------------------------------------------------------

def serie_fibonacci(numero):
    fibonacci = [0, 1]  # Lista inicial con los dos primeros números de la serie
    
    while True:
        siguiente_numero = fibonacci[-1] + fibonacci[-2]  # Calculamos el siguiente número de la serie
        
        if siguiente_numero > numero:  # Si el siguiente número excede el número dado, terminamos el bucle
            break
        
        fibonacci.append(siguiente_numero)  # Agregamos el siguiente número a la lista
    
    return fibonacci

resultado=fibonacci(34)
print(resultado)
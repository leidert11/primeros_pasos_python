numeros = [4,7,2]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)

#redoneando a 6 decimales
numero = round(12.345678,1)

#retorna False -> 0, vacio, False, None \ True -> distinto a 0, True, cadena, datos no vacio
resultado_bool = bool("sdsadsa")

#retorna True, si todos los valores son verdaderos
resultado_all = all([0,"true",[344,23]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(numero_mas_alto)
print(numero_mas_bajo)
print(numero)
print(resultado_bool)
print(resultado_all)
print(suma_total)
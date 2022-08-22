#1. Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, 
#   desde el número (como elemento 0) hasta 0 (como último elemento). Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def cuenta_regresiva(numero):
    lista = []
    for i in range(numero, -1, -1):
        lista.append(i)
    return lista
print(cuenta_regresiva(5))


#2. Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#   Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]
print(imprimir_y_devolver([1,2]))


#3. Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#   Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def primero_mas_longitud(lista):
    return lista[0] + len(lista)
print(primero_mas_longitud([1,2,3,4,5]))



#4. Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores 
#   que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#   Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#   Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False
    listaNueva = []
    for i in range(0,len(lista)):
        if lista[i] > lista[1]:
            listaNueva.append(lista[i])
    print(len(listaNueva))
    return listaNueva

print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))



#5. Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud 
#   sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#   Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#   Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def length_and_value(tamaño, valor):
    lista = []
    for i in range(0, tamaño):
        lista.append(valor)
    return lista

print(length_and_value(4,7))
print(length_and_value(6,2))
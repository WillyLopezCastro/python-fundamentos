num1 = 42 #declaracion variable, int
num2 = 2.3 #declaracion variable, float
boolean = True #tipos de datos, primitivo, booleano
string = 'Hello World' #tipos de datos, primitivo, str
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declaracion variable, lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declaracion variable, diccionario
fruit = ('blueberry', 'strawberry', 'banana') #declaracion variable, tupla
print(type(fruit)) #verificacion de tipo
print(pizza_toppings[1]) #imprime un valor de una lista
pizza_toppings.append('Mushrooms') #agregar valor al final de la lista
print(person['name']) #imprime el valor de una llave dentro de un diccionario
person['name'] = 'George' #cambia el valor de una llave dentro de un diccionario
person['eye_color'] = 'blue' #agrega una nueva llave y valor al diccionario
print(fruit[2]) #imprime el valor de un elemento de la tupla

if num1 > 45: #condicionales
    print("It's greater")
else: #condicionales
    print("It's lower")

if len(string) < 5: #condicionales
    print("It's a short word!")
elif len(string) > 15: #condicionales
    print("It's a long word!")
else: #condicionales
    print("Just right!")

for x in range(5): #bucle for
    print(x)
for x in range(2,5): #bucle for
    print(x)
for x in range(2,10,3): #bucle for
    print(x)
x = 0
while(x < 5): #bucle while
    print(x)
    x += 1

pizza_toppings.pop() #elimina el último elemento de la lista
pizza_toppings.pop(1) #elimina un valor especifico de la lista

print(person) #imprime el contenido del diccionario
person.pop('eye_color') #elimina la llave y el valor del diccionario
print(person) #imprime el contenido del diccionario

for topping in pizza_toppings: #bucle for
    if topping == 'Pepperoni': #secuencia
        continue #continuar
    print('After 1st if statement')
    if topping == 'Olives': #secuencia
        break #interrumpir

def print_hello_ten_times(): #funcion, parametro
    for num in range(10): #argumento
        print('Hello') #retorno

print_hello_ten_times()

def print_hello_x_times(x): #funcion, parametro
    for num in range(x): #argumento
        print('Hello') #retorno

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #funcion, parametro
    for num in range(x): #argumento
        print('Hello') #retorno

print_hello_x_or_ten_times() #NameError: el nombre <'print_hello_x_or_ten_times'> no esta definido
print_hello_x_or_ten_times(4) #NameError: el nombre <'print_hello_x_or_ten_times'> no esta definido


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
""""Clase de If/Else/Elif."""

my_number = int(input('Ingresa un numero entero: '))


if  5 > my_number: 
    print(f'5 es mayor que {my_number}') 
elif 5 == my_number:                     #Cuando elif se cumple, lo demás ya no se pregunta
    print(f'{my_number} es igual a 5') 
else:
    print(f'5 es menor a {my_number}')
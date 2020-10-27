"""Clase de for."""

names=('Abrahan', 'César', 'Daniel','Daniela','Diego','Edgar')

for name in names:
    print(f'Student: {name}')
    """if name=='Daniela':
        break  # si se detiene tampoco se toma en cuenta el else, else es otra iteración del for"""
else: 
    print('No more names')  # else por si solo es una condicional, se ocupa con if, for, while


string = 'Mauricio'

for char in string:
   if char != 'i': 
    print(char) 
   else: 
    print('Out of the for') 

 

 numbers = []

 for number in range(0, 21, 2):
    numbers.append(number)

print(numbers)
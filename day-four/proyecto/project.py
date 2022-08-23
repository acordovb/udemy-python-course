from random import randint
n_random = randint(1, 100)
intentos = 0
name = input('Ingresa tu nombre: ')
print(f'Hola {name}, he pensado un numero entre el 1 y el 100 y tienes solo {intentos} para adivinarlo. \n\
Cual crees que es el numero?')
numero = 0
while intentos<8:
    numero = int(input('Ingresa un numero: '))
    if numero < 1 or numero > 100:
        print('El numero no esta permitido dado que es mayor a 100 o menor que 1')
    elif numero < n_random:
        print('Tu respuesta es incorrecta, has elegido un numero menor al numero secreto.')
    elif numero > n_random:
        print('Tu respuesta es incorrecta, has elegido un numero mayor al numero secreto.')
    elif numero==numero:
        break
    intentos -=1
if numero == n_random:
    print(f'Has ganado, te ha tomado {intentos} intentos')
else:
    print('PERDISTE')

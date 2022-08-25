# El programa debe imprimir cada número del 1 al 100 por turnos
# Si el número es divisible por 3, debe imprimir Fizz en vez del número
# Si el número es divisible por 5, debe imprimir Buzz en vez del número
# Si el número es divisible por 3 y 5, debe imprimir FizzBuzz en vez del número

for number in range(1, 101):
    if number % 3 == 0 and number %5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

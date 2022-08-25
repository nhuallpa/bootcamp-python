# El programa debe calcular el puntaje mas alta de los estudiantes
print('Ingrese una lista de puntajes de estudiantes separando con espacios:')
ingreso = input()
puntaje_estudiantes = ingreso.split()
for indice in range(0, len(puntaje_estudiantes)):
    puntaje_estudiantes[indice] = int(puntaje_estudiantes[indice])
## Luego de aca
puntaje_maximo = 0
for puntaje in puntaje_estudiantes:
    if puntaje > puntaje_maximo:
        puntaje_maximo = puntaje

print('El puntaje mas alto es: ' + str(puntaje_maximo))
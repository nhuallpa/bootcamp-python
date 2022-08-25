# El programa debe calcular el altura mas alta de los estudiantes
print('Ingrese una lista de alturas de estudiantes separando con espacios:')
ingreso = input()
alturas_estudiantes = ingreso.split()
for indice in range(0, len(alturas_estudiantes)):
    alturas_estudiantes[indice] = int(alturas_estudiantes[indice])
## Luego de aca
numero_estudiantes = 0
for altura in alturas_estudiantes:
    numero_estudiantes += 1

suma_alturas = 0
for altura in alturas_estudiantes:
    suma_alturas += altura

print('La altura promedio es: ' + str(round(suma_alturas / numero_estudiantes)))
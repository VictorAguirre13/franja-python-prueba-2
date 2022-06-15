#Ejercicio 3 (30 puntos): 

#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


def valordepi():
    return 3.14


def area(radio):
    pi = valordepi()
    return pi*radio**2
print(f'Area = {area(10)}')

def volumen(radio,altura):
    volumen = area(radio)*altura
    return volumen


print(f'Volumen = {volumen(3,5)}')
#Ejercicio 2 (30 puntos): Escriba un programa que pida dos palabras 
# y diga si riman o no. Si coinciden las últimas tres letras tiene que decir que riman. 
# Si coinciden sólo las últimas dos tiene que decir que riman un poco. Y si no coinciden, 
# decir que no riman. Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices



p1 = input("Escriba una palabra: ")
p2 = input("Escriba otra palabra: ")
 
palabra1_ultimas_tres = p1[-3:] 
palabra2_ultimas_tres= p2[-3:]
palabra1_ultimas_dos = p1[-2:]
palabra2_ultimas_dos = p2[-2:]
 
if palabra1_ultimas_tres == palabra2_ultimas_tres:
    print("Las palabras riman")
elif palabra1_ultimas_dos == palabra2_ultimas_dos:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")
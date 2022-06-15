def mas_larga(lista):
	palabra_grande = len(lista[0])
	palabra_x = lista[0]

	for palabra in lista:
		if palabra_grande <= len(palabra):
			palabra_x = palabra
			palabra_grande = len(palabra)
		else:
			palabra_x = palabra_x

	print(palabra_x)


lista = ["a", "Victorlafixa", "Aguirreelmeocorte"]
mas_larga(lista)
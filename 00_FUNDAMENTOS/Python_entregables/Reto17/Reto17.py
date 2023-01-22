'''
Reto 17: Partiendo de la siguiente tupla:
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Realiza las siguientes operaciones:
  Encontrar los elementos de 3 a 5
  Encontrar los 6 primeros elementos
  Muestra la tupla desde el 5 elemento hasta el final
  Muestra toda la tupla haciendo uso de [:]
  Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
  Devuelve la tupla con un salto cada 4 elementos
  Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
'''
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

print(tupla[2:5])
print(tupla[:6])
print(tupla[4:])
print(tupla[:])
print(tupla[1:9:2])
print(tupla[0:len(tupla):5])
print(tupla[8:0:-1])
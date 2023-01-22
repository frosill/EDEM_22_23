'''
RETO 2: Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
'''

def Reto2():
  numero_inicial=6
  numero_final=50
  numeros_impares=range(numero_inicial-1,numero_final,2)
  print(*numeros_impares)
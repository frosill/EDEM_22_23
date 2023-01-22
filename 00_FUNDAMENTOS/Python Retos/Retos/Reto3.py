'''
RETO 3: Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
'''
def Reto3() :
  numeros = range(1,101,1)
  numeros_invertidos=reversed(numeros)
  print(*numeros_invertidos)
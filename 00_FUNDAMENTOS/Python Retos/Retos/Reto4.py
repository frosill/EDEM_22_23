'''
RETO4: Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
'''
def Reto4():
  miLista =  [1,2,3,4,5,6,7,8,9,10]
  miListaInvertida = reversed(miLista)
  print(*miListaInvertida)
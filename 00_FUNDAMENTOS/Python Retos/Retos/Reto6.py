'''
RETO 6: Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

def Reto6 () :
  EdadFinal = 18
  EdadPedida = int(input("Hola, ¿Cuantos años tienes? "))

  if EdadPedida < EdadFinal:
    print("Eres menor de edad")
  else:
    print("Eres mayor de edad")


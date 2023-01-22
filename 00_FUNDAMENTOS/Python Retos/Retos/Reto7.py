'''
Reto 7: Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
'''

def Reto7():

  contrasena = 'ContrAseÑa'
  textoIntroducido = str(input("Introduce un texto: "))

  if contrasena.lower() == textoIntroducido.lower():
    print('Las dos cadenas tienen los mismos caracteres')
  else:
    print('Las dos cadenas no tienen los mismos carcateres')

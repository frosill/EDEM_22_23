'''
Reto 9 Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no

¿Cómo saber si un año es bisiesto o no?
Es bisiesto si es divisible entre 4.
Pero no es bisiesto si solo es divisible entre 100.
Pero sí es bisiesto si es divisible entre 400. ©copyright los40.com
'''

def Reto9(anio):

  if (anio % 400 == 0 and anio % 100 == 0) or anio % 4 == 0 and anio % 100 != 0 :
    print(f"El año {anio} es bisiesto")
    return True 
  
  else :
    print(f"El año {anio} no es bisiesto")
    return False
  
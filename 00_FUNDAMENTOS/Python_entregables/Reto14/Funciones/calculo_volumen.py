'''
FUNCIONES PARA EL CALCULO DEL AREA DEL CIRCULO Y POSTERIOR CALCULO DEL VOLUMNE DEL CILINDRO
'''

from math import pi     

def area_circulo(radio) -> float: #CALCULO AREA CIRCULO
  
  return pi*radio**2


def volumen_cilindro(radio: float, altura: float) -> float: #CALCULO VOLUMEN CILINDRO MEDIANTE EL AREA DEL CIRCULO

  base:float =  area_circulo(radio)
  volumen = round(base * altura,2)

  return print(volumen)
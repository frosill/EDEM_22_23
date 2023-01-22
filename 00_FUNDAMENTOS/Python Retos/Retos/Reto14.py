'''
Reto 14: Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
'''

from Retos.Reto13 import area_circulo

def volumen_cilindro(radio: float, altura: float) -> float:

  base:float =  area_circulo(radio)
  volumen = round(float(base) * float(altura),2)

  return volumen

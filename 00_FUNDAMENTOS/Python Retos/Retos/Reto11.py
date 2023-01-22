'''
Reto 11: Escribe un programa que pida al usuario los siguientes datos por consola:
Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula"
'''

def almacena_pelicula():

  titulo = str(input("Introduzca el titulo de la película: "))
  director = str(input("Introduzca el director de la película: "))
  anio = int(input("Introduzca el año de la película: "))
  pais = str(input("Introduzca el pais dónde se rodoó la pelicula: "))

  global pelicula

  pelicula = {'titulo':'','director':'','año':0,'pais':''}

  pelicula['titulo'] = titulo
  pelicula['director'] = director
  pelicula['año'] = anio
  pelicula['pais'] = pais

  print(pelicula)
  
  
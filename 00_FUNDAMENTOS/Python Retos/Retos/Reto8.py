'''
Reto 8: Escribe un programa que pueda decirte si un número (número entero) es primo o no
'''

def Reto8():

  numeroSolicitado = int(input('Introduzca un numero: '))

  for n in range(2,numeroSolicitado): # Vemos si desde el 2 al numeroSolicitado-1  es divisible
    if numeroSolicitado % n == 0 :
      print(f"El {numeroSolicitado} no es primo: {n} divisor") # 
      return False

  print(f"El numero {numeroSolicitado} es primo")
  return True
  
      
  
      
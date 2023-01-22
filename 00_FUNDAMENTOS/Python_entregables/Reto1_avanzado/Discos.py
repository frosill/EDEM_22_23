'''
RETO1 AVANZADO
Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock almacenado durante meses, se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.
Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.

Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final de la compra.

Nombre
Artista
Año
Precio
Género (solo pueden ser de los siguientes):
  Pop
  Electro
  Reggaeton
  Rock
  Metal
  Death Metal
  Black Metal
'''
from datetime import date



discos = {            # Definimos el diccionario hasta la linea 68
    'Pop' : {
        'Nombre' : 'As it was', 
        'Artista' : 'Harry Styles',
        'Año': 1998,
        'Precio': 12
        },
    'Electro' : {
      'Nombre' : 'Something New', 
      'Artista' : 'Swedish House Mafia',
      'Año': 2013,
      'Precio': 10
      },
    'Reggaeton' : {
      'Nombre' : 'PARAISO', 
      'Artista' : 'Mora',
      'Año': 2022,
      'Precio': 22
      },
    'Rock' : {
      'Nombre' : 'Disco Rock', 
      'Artista' : 'Red Hot Chilli Peppers',
      'Año': 1996,
      'Precio': 12
      },
    'Metal' : {
      'Nombre' : 'Disco Metal', 
      'Artista' : 'Metallica',
      'Año': 1983,
      'Precio': 7
      },
    'Death Metal' : {
      'Nombre' : 'Disco Death Metal', 
      'Artista' : 'ACDC',
      'Año': 1972,
      'Precio': 9
      },
    'Black Metal' : {
      'Nombre' : 'Disco Black Metal', 
      'Artista' : 'Linkin Park',
      'Año': 1972,
      'Precio': 9
      },    
    }

print("Estos son los discos de música disponibles en la tienda: ") # Mostrar todos los discos por pantalla
for genero, propiedades in discos.items():  
    print("\n" + genero)
    nombre = propiedades['Nombre']
    artista = propiedades['Artista']
    anio = propiedades['Año']
    precio = propiedades['Precio']

    print(f"Nombre: {nombre} \nArtista: {artista} \nAño: {anio} \nPrecio: {precio}")

userInput = str(input("\nIntroduzca el genero del disco que desea comprar: "))
pulsaCero = int(input(f"\nHas elegido {userInput}, pulse la tecla 0 para continuar"))

  #Vamos comprobando que disco quiere el usuario y si pulsa 0 se muestra su ticket de compra por consola
if userInput == 'Pop' and pulsaCero == 0:   
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Pop'].get('Precio')
    fecha = date.today()
    
    ahorro = 0

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

elif userInput == 'Electro' and pulsaCero == 0:
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Electro'].get('Precio')
    fecha = date.today()

    ahorro = round(0.3*precio, 2)

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

elif userInput == 'Reggaeton' and pulsaCero == 0:
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Reggaeton'].get('Precio')
    fecha = date.today()

    ahorro = 0

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

elif userInput == 'Rock' and pulsaCero == 0:
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Rock'].get('Precio')
    fecha = date.today()

    ahorro = 0

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

elif userInput == 'Metal' and pulsaCero == 0:
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Metal'].get('Precio')
    fecha = date.today()

    ahorro = 0

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

elif userInput == 'Death Metal' and pulsaCero == 0:
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Death Metal'].get('Precio')
    fecha = date.today()

    ahorro = 0

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

elif userInput == 'Black Metal' and pulsaCero == 0:
    
    print("\nTu compra se ha realizado con exito!\nDetalles de su compra: ")

    precio = discos['Black Metal'].get('Precio')
    fecha = date.today()

    ahorro = round(0.3*precio, 2)

    print(f"\nFecha de compra: {fecha}\nTe has ahorrado {ahorro}€\nEl precio final de tu compra es {precio - ahorro}€")

else:

    print("Lo sentimos, actualmente no disponemos del genero que ha solicitado o no a insertado 0 para continuar con el proceso de compra")
    
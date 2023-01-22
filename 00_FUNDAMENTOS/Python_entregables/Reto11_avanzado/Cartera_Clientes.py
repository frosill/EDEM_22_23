'''
Reto 11: Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean).
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS os clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa
'''

from Classes.Cliente import Cliente

# Inicialización clientes en cartera actualmente
cliente1 = Cliente('45464148J', 'Joaquin', 'Reyes Gomez', '694564123','joarego@gmail.com', preferente = False)
cliente2 = Cliente('45464348D', 'Fernando', 'Sebastian Lopez', '642789453','nandose@gmail.com', preferente = True)
cliente3 = Cliente('35428342D', 'Paco', 'Beltran Torres', '621248795','pabeto@gmail.com', preferente = True)
cliente4 = Cliente('66666666F', 'Pablo', 'Gonzalez Martinez', '654987321', 'pagonza@edem.es', preferente = False)

#Inicialización lista de clientes
Clientes = [cliente1, cliente2, cliente3, cliente4]

#Inicializamos el valor de seleccion
seleccion = 0

#Logica de selección del menu
# Si introducimos 6 terminamos el programa
while seleccion != 6:

  seleccion = int(input('\n¡Bienvenido a la gestión de cartera de clientes! Seleccione una de las siguientes opciones para continuar:\n\n\t(1) Añadir un cliente\n\t(2) Eliminar cliente por NIF\n\t(3) Mostrar cliente por NIF\n\t(4) Listar todos los clientes\n\t(5) Mostrar todos los clientes preferentes\n\t(6) Finalizar programa\n\nIntroduzca su selección: '))
# Si introducimos 1: introducimos por pantalla los datos edl nuevo cliente que vamos a añadir
  if seleccion == 1:
  
    print(f"\nHas seleccionado ({seleccion}): Has seleccionado añadir un nuevo cliente")

    nombre = str(input("Introduzca el Nombre: "))
    apellidos = str(input("Introduzca los Apellidos: "))
    NIF = str(input("Introduzca el NIF: "))
    telefono = str(input("Introduzca el número telefono: "))
    email = str(input("Introduzca el email: "))
    preferente = bool(input("Introduzca si el nuevo cliente es preferente: True/False \n"))
  
    nuevoCliente = Cliente(NIF, nombre, apellidos, telefono, email, preferente)
    Clientes.append(nuevoCliente)

# Si introducimos 2: Eliminamos un cliente de la carteta según el NIF
  elif seleccion == 2:

    print(f"\nHas seleccionado ({seleccion}): Has seleccionado eliminar un cliente por NIF")
  
    NIF = str(input("Introduzca el NIF: "))

    for n in Clientes:
      if n.NIF == NIF:
        Clientes.remove(n)

# Si introducimos 3: Mostramos un cliente de la carteta según el NIF
  elif seleccion == 3:

    print(f"\nHas seleccionado ({seleccion}): Has seleccionado mostrar un cliente por NIF")

    NIF = str(input("Introduzca el NIF: "))

    for n in Clientes:
      if n.NIF == NIF:
         print(f'\n\nNIF: {n.NIF}\nNombre: {n.nombre}\nApellidos: {n.apellidos}\nTelefono: {n.telefono}\nEmail:{n.email}\nPreferente: {n.preferente} ')

# Si introducimos 4: Listar todos los clientes
  elif seleccion == 4:

    print(f"\nHas seleccionado ({seleccion}): Has seleccionado mostrar todos los clientes")
    
    for n in Clientes:
      print(f'\n\nNIF: {n.NIF}\nNombre: {n.nombre}\nApellidos: {n.apellidos}\nTelefono: {n.telefono}\nEmail:{n.email}\nPreferente: {n.preferente}')

# Si introducimos 5: Mostramos por pantalla los clientes preferentes
  elif seleccion == 5:

    print(f"\nHas seleccionado ({seleccion}): Se mostrarán todos los clientespreferentes")
    
    for n in Clientes:
      if n.preferente == True:
        print(f'\n\nNIF: {n.NIF}\nNombre: {n.nombre}\nApellidos: {n.apellidos}\nTelefono: {n.telefono}\nEmail:{n.email}\nPreferente: {n.preferente}')

  elif seleccion == 6:
    print(f'Has seleccionado ({seleccion}): El programa ha finalizado')
    break

  else:
    print(f"La opción ({seleccion}) no está disponible\n")
    
    seleccion = int(input('Vuelva a introducir una de las opciones validas:\n\n\t(1) Añadir un cliente\n\t(2) Eliminar cliente por NIF\n\t(3) Mostrar cliente por NIF\n\t(4) Listar todos los clientes\n\t(5) Mostrar todos los clientes preferentes\n\t(6) Finalizar programa\n\n Inroduzca su selección: '))
  
  
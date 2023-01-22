'''
Creación del objeto cliente para operar con el en Cartera_Clientes.py
'''

class Cliente():

    #Inicializamos atributos
    def __init__(self, NIF : str, nombre : str, apellidos : str, telefono: str, email : str, preferente: bool):

        self.NIF = NIF
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.preferente = preferente
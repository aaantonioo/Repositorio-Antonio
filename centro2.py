
from cancha import Cancha
from persona import Clientes, Empleado
from resrva import Reserva


class Centro:
    def __init__(self, nombre, direccion, lista_canchas, lista_clientes):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = lista_canchas
        self.lista_clientes = lista_clientes
    

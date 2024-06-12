
from cancha import Cancha
from persona import Clientes, Empleado
from reserva import Reserva


class Centro:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = []
        self.lista_clientes = []
        self.lista_empleado = []
        self.lista_reserva = []
    
    def menu(self):
        while True:
            print("1. Canchas")
            print("2. Clientes")
            print("3. Empleado")
            print("4. Reserva")
            print("5. Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                self.canchas()
            elif opcion == 2:
                self.clientes()
            

    def canchas(self):
        while True:
            def menu():
                print("1. Crear cancha")
                print("2. Agregar cancha")
                print("3. Listas cancha por deporte")
                print("4. Quitar cancha")
                print("5. Salir")
                opcion = int(input("Opcion: "))

                if opcion == 1:
                    Cancha.crear_cancha()
                elif opcion == 2:
                    Cancha.agregar_cancha()
                elif opcion == 3:
                    Cancha.listar_canchas_por_deporte()
                elif opcion == 4:
                    Cancha.quitar_cancha()
                elif opcion == 5:
                    pass
                
    def clientes(self):
        while True:
            def menu():
                print("1. Crear cliente")
                print("2. Agregar cliente")
                print("3. Quitar cliente")
                print("4. Listar clientes morosos")
                opcion = int(input("Opcion: "))

                if opcion == 1:
                    Clientes.crear_cliente()
                elif opcion == 2:
                    Clientes.agregar_cliente()
                elif opcion == 3:
                    Clientes.quitar_cliente()
                elif opcion == 4:
                    Clientes.clientes_morosos()
                
    def empleado(self):
        while True:
            def menu():
                print("1. Crear empleado")
                print("2. Registrar empleado")
                print("3. Asignar tarea")

                opcion = int(input("Opcion: "))

                if opcion == 1:
                    Empleado.crear_empleado()
                elif opcion == 2:
                    Empleado.registrar_empleado()
                elif opcion == 3:
                    Empleado.asignar_tarea()
                




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
            elif opcion == 3:
                self.empleado()
            elif opcion == 4:
                self.reserva()
            elif opcion == 5:
                pass


    def canchas(self):
        while True:
            
            print("1. Crear y agregar cancha")
            print("2. Listas cancha por deporte")
            print("3. Quitar cancha")
            print("4. Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                Cancha.crear_cancha()
            elif opcion == 2:
                Cancha.listar_canchas_por_deporte()
            elif opcion == 3:
                Cancha.quitar_cancha()
            elif opcion == 4:
                pass
                
    def clientes(self):
        while True:
            
            print("1. Crear cliente y agregar cliente")
            print("2. Quitar cliente")
            print("3. Listar clientes morosos")
            print("4. Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                Clientes.crear_cliente()
            elif opcion == 2:
                Clientes.quitar_cliente()
            elif opcion == 3:
                Clientes.clientes_morosos()
            elif opcion == 4:
                pass
                
    def empleado(self):
        while True:
           
            print("1. Crear empleado")
            print("2. Registrar empleado")
            print("3. Asignar tarea")
            print("4. Quitar tarea")

            opcion = int(input("Opcion: "))

            if opcion == 1:
                Empleado.crear_empleado()
            elif opcion == 2:
                Empleado.registrar_empleado()
            elif opcion == 3:
                Empleado.asignar_tarea()
            elif opcion == 4:
                Empleado.quitar_tarea()
    
    def reserva(self):
        while True:
            print("1. Crear reserva")
            print("2. Registrar reserva")
            print("3. Registrar pago")
            print("4. Mostrar saldo")
            print("5. Listar reservas por cancha")
            print("6. Listar reservas por cliente")
            print("7. Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                Reserva.crear_reserva()
            elif opcion == 2:
                Reserva.registrar_reserva()
            elif opcion == 3:
                Reserva.registrar_pago()
            elif opcion == 4:
                Reserva.mostrar_saldo()
            elif opcion == 5:
                Reserva.listar_reservas_por_cancha()
            elif opcion == 6:
                Reserva.listar_reservas_por_cliente()
            elif opcion == 7:
                pass



def main():
    nombre = input("Introduce el nombre del centro: ")
    direccion = input("Introduce la direccion del centro: ")
    centro = Centro(nombre, direccion)
    centro.menu()

main()    



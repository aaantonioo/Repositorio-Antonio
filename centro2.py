
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
                cancha = Cancha.crear_cancha()
                if cancha:
                    cancha.agregar_cancha(self.lista_canchas)

            elif opcion == 2:
                deporte = input("Ingrese el deporte para listar las canchas: ")
                canchas = Cancha.listar_canchas_por_deporte(self.lista_canchas, deporte)
                if canchas:
                    for cancha in canchas:
                        print(f"Número: {cancha.numero}, Deporte: {cancha.deporte}, Precio: {cancha.precio}, Habilitada: {'Sí' if cancha.habilitada else 'No'}")
                else:
                    print(f"No hay canchas registradas para el deporte {deporte}.")

            elif opcion == 3:
                numero_cancha = int(input("Ingrese el número de la cancha a quitar: "))
                cancha = next((c for c in self.lista_canchas if c.numero == numero_cancha), None)
                if cancha:
                    cancha.quitar_cancha(self.lista_canchas)
                else:
                    print(f"No se encontró una cancha con número {numero_cancha}.")

            elif opcion == 4:
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                
    def clientes(self):
        while True:
            
            print("1. Crear cliente y agregar cliente")
            print("2. Listar clientes")
            print("3. Quitar cliente")
            print("4. Listar clientes morosos")
            print("5. Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                cliente = Clientes.crear_cliente(self)
                if cliente:
                    cliente.agregar_cliente(self.lista_clientes)
            elif opcion == 2:
                for cliente in self.lista_clientes:
                    print(f"ID: {cliente.identificador}, Nombre: {cliente.nombre} {cliente.apellido}, Teléfono: {cliente.telefono}, Saldo: {cliente.saldo}")
            elif opcion == 3:
                id = int(input("Dime el id del cliente que quieres eliminar: "))
                cliente = next((c for c in self.lista_clientes if c.identificador == id), None)
                if cliente:
                    cliente.quitar_cliente(self.lista_clientes)
                break

            elif opcion == 4:
                clientes_morosos = Clientes.clientes_morosos(self.lista_clientes)
                if clientes_morosos:
                    for cliente in clientes_morosos:
                        print(f"ID: {cliente.identificador}, Nombre: {cliente.nombre} {cliente.apellido}, Saldo: {cliente.saldo}")
            elif opcion == 5:
                break
                
    def empleado(self):
        while True:
           
            print("1. Crear empleado y registrar")
            print("2. Asignar tarea")
            print("3. Quitar tarea")
            print("4. Salir")
            

            opcion = int(input("Opcion: "))

            if opcion == 1:
                cliente = Empleado.crear_empleado(self)
                if cliente:
                    cliente.agregar_empleado(self.lista_empleado)
            elif opcion == 2:
                        
                        id_empleado = int(input("Ingrese el índice del empleado al que desea asignar tarea: ")) - 1
                        empleado_seleccionado = self.lista_empleado[id_empleado]
                        tarea = input("Ingrese la tarea que desea asignar: ")

                        id_cancha = int(input("Ingrese el índice de la cancha que desea asignar al empleado: ")) - 1
                        cancha_seleccionada = self.lista_canchas[id_cancha]

                        empleado_seleccionado.asignar_tarea(tarea, cancha_seleccionada)
                        print(f"Tarea '{tarea}' asignada exitosamente a {empleado_seleccionado.nombre} {empleado_seleccionado.apellido}.")
                    
            elif opcion == 3:
                nombre = str(input("Dime el nombre del empleado que quieres quitar: "))
                empleado = next((e for e in self.lista_empleado if e.nombre == nombre), None)
                if empleado:
                    empleado.quitar_empleado(self.lista_empleado)
                break
            elif opcion == 4:
                break
    
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
                if not self.lista_canchas:
                    print("No hay canchas registradas. Debe agregar al menos una cancha antes de crear una reserva.")
                else:
                    reserva = Reserva.crear_reserva(self.lista_clientes, self.lista_canchas)
                    if reserva:
                        reserva.registrar_reserva(self.lista_reservas)

            elif opcion == 2:
                if not self.lista_canchas:
                    print("No hay canchas registradas.")
                else:
                    numero_cancha = int(input("Ingrese el número de la cancha para listar las reservas: "))
                    Reserva.listar_reservas_por_cancha(self.lista_reservas, numero_cancha)

            elif opcion == 3:
                if not self.lista_clientes:
                    print("No hay clientes registrados.")
                else:
                    identificador_cliente = input("Ingrese el identificador del cliente para listar las reservas: ")
                    Reserva.listar_reservas_por_cliente(self.lista_reservas, identificador_cliente)

            elif opcion == 4:
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")



def main():
    nombre = input("Introduce el nombre del centro: ")
    direccion = input("Introduce la direccion del centro: ")
    centro = Centro(nombre, direccion)
    centro.menu()

main()    



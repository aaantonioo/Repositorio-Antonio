class Clientes:
    def __init__(self, nombre, apellido, telefono, identifcador):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificador = identifcador
        self.saldo = 0 
    
    def crear_cliente(self,lista_cliente):
        nombre = str(input("Nombre del cliente: "))
        apellido = str(input("Apellido del cliente: "))
        telefono = int(input("Telefono del cliente: "))
        id = int(input("Id del cliente: "))
        lista_cliente.append(self)
        return Clientes(nombre, apellido, telefono, id)

    
    def quitar_cliente(self,lista_cliente):
        identifcador = int(input("Dime el identificador del cliente que quieres eliminar: "))
        for cliente in lista_cliente:
            if cliente.id == identifcador:
                self.clientes.remove(cliente)
                print(f"Cliente con el id eliminado.")
                return
            
        print(f"No hay nigun cliente con ese id")
    

    def clientes_morosos(lista_cliente):
        return [ cliente for cliente in lista_cliente if cliente.saldo < 0]
    

class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.desocupado = True
        self.lista_tareas = []
    
    def crear_empleado(self, lista_empleados):
        nombre = str(input("Nombre del empelado: "))
        apellido = str(input("Apellido del empleado: "))

        lista_empleados.append(self)
        return Empleado(nombre, apellido)
    
    def asignar_tarea(self, tarea, cancha,lista_empleados):
        nombre_usuario = str(input("Dime el nombre del empleado que vas asignar una tarea: "))
        if nombre_usuario in lista_empleados:
            self.lista_tareas.append(tarea)
            self.desocupado = False
            cancha.lista_canchas.append(self)
    
    def quitar_tarea(self,tarea):
        nombre_empleado = str(input("A que empleado le quieres quitar la tarea: "))
        for empleado in self.lista_tareas:
            if empleado.nombre == nombre_empleado:
                self.lista_tareas.remove(empleado)
                print(f"Cliente con el id eliminado.")
                return
            
            if not self.tareas:
                self.desocupado = True
        print("No hay ningun empelado con ese nombre")
    


    

    

    
   

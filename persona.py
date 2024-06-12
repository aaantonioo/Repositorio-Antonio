class Clientes:
    def __init__(self, nombre, apellido, telefono, identifcador):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificador = identifcador
        self.saldo = 0 
    
    def crear_cliente():
        nombre = str(input("Nombre del cliente: "))
        apellido = str(input("Apellido del cliente: "))
        telefono = int(input("Telefono del cliente: "))
        id = int(input("Id del cliente: "))

        return Clientes(nombre, apellido, telefono, id)

    def agregar_cliente(self,lista_cliente):
        lista_cliente.append(self)
    
    def quitar_cliente(self,id):

        for cliente in self.clientes:
            if cliente.id == id:
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
    
    def crear_empleado():
        nombre = str(input("Nombre del empelado: "))
        apellido = str(input("Apellido del empleado: "))
        return Empleado(nombre, apellido)
    
    def registrar_empleado(self, lista_empleados):
        lista_empleados.append(self)
    
    def asignar_tarea():
        
    

    

    
   

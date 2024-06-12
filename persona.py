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
        telefono = int(input("Dime el telefono del cliente: "))
        id = int(input("Dime el id del cliente: "))

        return Clientes(nombre, apellido, telefono, id)

    def agregar_cliente(self,lista_cliente):
        lista_cliente.append(self)
    
    def quitar_cliente(self,id):

        for cliente in self.clientes:
            if cliente.id == id:
                self.clientes.remove(cliente)
                print(f"Cliente con identificador {id} eliminado.")
                return
            
        print(f"No se encontró ningún cliente con ese identificador")
    

    def clientes_morosos(lista_cliente):
        return [cliente for cliente in lista_cliente if cliente.saldo < 0]

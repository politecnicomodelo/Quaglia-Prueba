class Colegio(object):
    listaPersonas=[]
    listaPlatos=[]
    listaPedidos=[]

    def __init__(self):
        self.listaPersonas = []
        self.listaPlatos = []
        self.listaPedidos = []

    def agregarPersona(self, persona):
        (self.listaPersonas).append(persona)

    def agregarPlato(self, platos):
        (self.listaPlato).append(platos)

    def agregarPedido(self, pedidos):
        (self.listaPedido).append(pedidos)




class Persona(object):
    Nombre=""
    Apellido=""

    def setNombre(self, nombre):
        self.Nombre=nombre

    def setApellido(self, apellido):
        self.Apellido=apellido

    def getDescuento(self):
        return 0

class Alumno(Persona):
    Division=""

    def setDivision(self, division):
        self.Division=division

class Profesor(Persona):
    Descuento=0

    def setDescuento(self, descuento):
        self.Descuento=descuento
    def getDescuento(self):
        return self.Descuento

class Plato(object):
    Nombre=""
    Precio=0

    def setNombre(self, nombre):
        self.Nombre=nombre

    def setPrecio(self, precio):
        self.Precio=precio

class Pedido(object):
    FechaCreacion = None
    Comprador = None
    HoraEntrega = ""
    Plato = None
    Entregado = False

    def setFechaCreacion(self, fecha):
        self.FechaCreacion=fecha

    def setComprador(self,comprador):
        self.Comprador=comprador

    def setHoraEntrega(self, hora):
        self.HoraEntrega=hora

    def setPlato(self, plato):
        self.Plato=plato

    def setEntregado(self, entregado):
        self.Entregado=entregado


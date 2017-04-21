class Vehiculo(object):
    Patente=""
    CantidadRuedas=0
    AnoFabricacion=0

    def setPatente(self, patente):
        self.Patente=patente

    def setCantidadRuedas(self, ruedas):
        self.CantidadRuedas=ruedas

    def setAnoFabricacion(self, ano):
        self.AnoFabricacion=ano

class Camioneta(Vehiculo):

    capacidadCarga=0

    def capacidadCarga(self, kilos):
        self.capacidadCarga=kilos

class Auto(Vehiculo):

    descapotable=True

    def setDescapotable(self, descapotable):
        self.setDescapotable=descapotable

class Empresa(object):
    listaCamionetas=[]
    listaAutos=[]

    def __init__(self):
        listaCamionetas = []
        listaAutos = []

    def AgregarAutos(self,autos):
        (self.listaAutos).append(autos)

    def AgregarCamioneta(self,camioneta):
        (self.listaCamionetas).append(camioneta)
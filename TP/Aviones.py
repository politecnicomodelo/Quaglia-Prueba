import datetime

class Avion (object):
    codigoUnico = ""
    cantidadPasajeros = 0
    cantidadTripulacion = 0

class Persona (object):
    Nombre=""
    Apellido=""
    FechaNacimiento = ""
    DNI = ""
    def diasVividos(self):
        now = datetime.datetime.now()
        fechaActual = now.strftime("½d-½m-½Y")
        fechaNacimiento = datetime.datetime.strptime(self.FechaNacimiento, "½d-½m-½Y")
        fechaActual = datetime.datetime.strptime(fechaActual, "½d-½m-½Y")
        return ((fechaActual - fechaNacimiento).days)

class Pasajero (Persona):
    Millas = 0
    VIP = False
    Necesidades= ""


class Piloto(Persona):
    modeloAviones = ""

class Servicio(Piloto):
    Idiomas = ""

class Vuelo(object):
    Avion = None
    Fecha = ""
    Hora = ""
    Origen = ""
    Destino = ""

    def __init__(self):
        self.Tripulacion = []
        self.Pasajeros = []

    def agregarTripulacion(self, tripulacion):
        self.Tripulacion.append(tripulacion)

    def agregarPasajero(self, pasajero):
        self.Pasajeros.append(pasajero)

    def Nomina(self):
        nomina=[]
        nombre1 = ""
        for persona in self.Pasajeros:
            nomina.append(persona.Nombre + " " + persona.Apellido)
        return nomina
    def joven(self):
        edades = []
        for persona in self.Pasajeros:
            edades.append(persona.diasVividos())
        chico = min(edades)
        for persona in self.Pasajeros:
            if persona.diasVividos() == chico:
                return persona.Nombre + " " + persona.Apellido

    def tripulacionMinima(self):
        if self.Avion.cantidadTripulacion > len(self.Tripulacion+1):
            return False
        else:
            return True
    def tripulacionAutorizada(self):
        noAuto = []
        for tripulante in self.Tripulacion:
            if self.Avion.codigoUnico not in tripulante.modeloAviones:
                noAuto.append(tripulante.Nombre + " " + tripulante.Apellido)
        return noAuto
    def especiales(self):
        VIPs= []
        Especiales=[]
        for persona in self.listaPasajeros:
            if persona.VIP == True:
                VIPs.append(persona)
            if persona.Necesidades != "":
                Especiales.append(persona)
        return VIPs, Especiales

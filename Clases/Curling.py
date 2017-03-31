class Jugador(object):

    Nombre = ""
    Fechanac = None
    Numero = 0

    def setNombre(self, nombre):
        self.Nombre=nombre

    def setFechanac(self, fechanac):
        self.Fechanac=fechanac

    def setNumero(self, numero):
        self.Numero=numero

class Equipo(object):

    Nombre = ""
    Barrio = ""
    Capitan = ""
    Disponibilidad = []
    listaJugadores = []

    def setNombre(self, nombre):
        self.Nombre=nombre

    def setBarrio(self, barrio):
        self.Barrio=barrio

    def setCapitan(self,numero):
        self.Capitan=numero

    def __init__(self):
        self.Disponibilidad=[]
        self.listaJugadores=[]

    def agregarJugador(self, jugador):
        for JugAct in self.listaJugadores:
            if JugAct.Numero == Jugador.Numero:
                return False

        (self.listaJugadores).append(jugador)

    def setDisponibilidad(self,turno):
        (self.Disponibilidad).append(turno)

class Partido(object):
    Dia = None
    Turno = ""
    Equipos = []

    def __init__(self):
        self.Equipos=[]

    def setDia(self, dia):
        self.Dia=dia

    def setTurno(self,turno):
        self.Turno=turno

    def setEquipo(self, equipo):
        (self.Equipos).append=[]

class Torneo(object):

    Equipos = []
    listaPartidos = []

    def __init__(self):
        self.listaEquipos = []
        self.listaPartidos = []

    def agregarEquipo(self, equipo):
        for EquipoAct in self.listaEquipos:
            if EquipoAct.Nombre == Equipo.Nombre:
                return False
        (self.Equipos).append(equipo)

    def agregarPartido(self,partido):
        (self.listaPartidos).append(partido)



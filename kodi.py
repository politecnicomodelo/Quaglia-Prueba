from Clases.Curling import *
from datetime import date

Jug1=Jugador()
Jug2=Jugador()
Jug3=Jugador()
Jug4=Jugador()
Jug5=Jugador()

Jug1.setNombre("eemesi")
Jug1.setNumero(10)


Jug6=Jugador()
Jug7=Jugador()
Jug8=Jugador()
Jug9=Jugador()
Jug10=Jugador()

Jug6.setNombre("jesus")
Jug6.setNumero(33)

Equipo1 = Equipo()

Equipo1.setNombre("Chaca")
Equipo1.setBarrio("San Martin")
Equipo1.setCapitan(10)

TNP=[False,False,False] #Turno no puede en ningun horiario
TM=[True,False,False]   #Turno mañana
TT=[False,True,False]   #Turno tarde
TN=[False,False,True]   #Turno noche
TMT=[True,True,False]   #Turno mañana y tarde
TMN=[True,False,True]   #Turno mañana y noche
TTN=[False,True,True]   #Turno tarde y noche
TMTN=[True,True,True]   #Turno mañana, tarde y noche

Equipo1.setDisponibilidad(TM)   #Lunes
Equipo1.setDisponibilidad(TT)   #Martes
Equipo1.setDisponibilidad(TN)   #Miercoles
Equipo1.setDisponibilidad(TMN)  #Jueves
Equipo1.setDisponibilidad(TTN)  #Viernes
Equipo1.setDisponibilidad(TMTN) #Sabado
Equipo1.setDisponibilidad(TNP)  #Domingo


Equipo1.agregarJugador(Jug1)    #Agrego jugadores
Equipo1.agregarJugador(Jug2)
Equipo1.agregarJugador(Jug3)
Equipo1.agregarJugador(Jug4)
Equipo1.agregarJugador(Jug5)

Equipo2=Equipo()

Equipo2.agregarJugador(Jug6)    #Agrego jugadores
Equipo2.agregarJugador(Jug7)
Equipo2.agregarJugador(Jug8)
Equipo2.agregarJugador(Jug9)
Equipo2.agregarJugador(Jug10)

Equipo2.setNombre("Atlanta")
Equipo2.setBarrio("Caballito")
Equipo2.setCapitan(33)

Equipo2.setDisponibilidad(TT)   #Lunes
Equipo2.setDisponibilidad(TN)   #Martes
Equipo2.setDisponibilidad(TNP)  #Miercoles
Equipo2.setDisponibilidad(TMN)  #Jueves
Equipo2.setDisponibilidad(TMTN) #Viernes
Equipo2.setDisponibilidad(TM)   #Sabado
Equipo2.setDisponibilidad(TNP)  #Domingo

LpmCup= Torneo()

LpmCup.agregarEquipo(Equipo1)   #Agrego equipos al torneo
LpmCup.agregarEquipo(Equipo2)


